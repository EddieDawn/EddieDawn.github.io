#!/usr/bin/env python3
"""Import one Notion Markdown export ZIP as an Astro post.

The importer deliberately does not call the Notion API. Export a single Notion
page as "Markdown & CSV", then run this script against the downloaded ZIP.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import sys
import tempfile
import zipfile
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path, PurePosixPath
from typing import Callable
from urllib.parse import quote, unquote, urlsplit, urlunsplit


PROJECT_ROOT = Path(__file__).resolve().parents[1]
IMAGE_EXTENSIONS = {".avif", ".gif", ".jpeg", ".jpg", ".png", ".svg", ".webp"}
FRONTMATTER_RE = re.compile(r"\A---\s*\n.*?\n---\s*\n", re.DOTALL)
H1_RE = re.compile(r"^(?P<marker>#)\s+(?P<title>.+?)\s*$")
DATE_METADATA_RE = re.compile(r"^(?:날짜|작성일|date)\s*:\s*(?P<value>.+?)\s*$", re.IGNORECASE)
FENCE_OPEN_RE = re.compile(r"^[ \t]{0,3}(?P<marker>`{3,}|~{3,})")
IMPORT_SOURCE_MARKER_RE = re.compile(
    r"<!-- notion-import-source: (?P<source_id>[a-z0-9-]+) -->"
)
KOREAN_DATE_RE = re.compile(r"(?P<year>\d{4})년\s*(?P<month>\d{1,2})월\s*(?P<day>\d{1,2})일")
ISO_DATE_RE = re.compile(r"(?P<year>\d{4})[-./](?P<month>\d{1,2})[-./](?P<day>\d{1,2})")
MARKDOWN_LINK_RE = re.compile(
    r"(?P<prefix>!?)\[(?P<label>[^\]]*)\]"
    r"\((?P<target><[^>]+>|[^\s)]+)(?P<link_title>\s+(?:\"[^\"]*\"|'[^']*'))?\)"
)
SLUG_RE = re.compile(r"^[a-z0-9]+(?:[a-z0-9-]*[a-z0-9])?$")
NOTION_ID_RE = re.compile(r"(?P<id>[0-9a-f]{32})$", re.IGNORECASE)
UUID_RE = re.compile(
    r"(?P<id>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})",
    re.IGNORECASE,
)


class ImportErrorWithHint(Exception):
    """A user-actionable import error."""


@dataclass
class AssetCopy:
    source_relative_path: Path
    destination: Path


@dataclass
class ImportPlan:
    zip_path: Path
    source_markdown: Path
    post_path: Path
    source_id: str
    title: str
    published_at: str
    body: str
    copied_assets: list[AssetCopy] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Notion Markdown export ZIP을 Astro 게시물로 가져옵니다.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("zip_path", type=Path, nargs="?", help="Notion에서 내보낸 Markdown & CSV ZIP 파일")
    parser.add_argument("--all", action="store_true", help="imports/ 안의 모든 ZIP을 한 번에 가져옵니다.")
    parser.add_argument("--imports-dir", type=Path, default=PROJECT_ROOT / "imports", help="--all에서 읽을 ZIP 폴더")
    parser.add_argument("--slug", help="개별 가져오기에 사용할 영문 slug (예: java-basic-syntax)")
    parser.add_argument("--source", help="ZIP 안에 Markdown 파일이 여러 개일 때 가져올 파일 경로")
    parser.add_argument("--overwrite", action="store_true", help="같은 slug의 Markdown 파일과 같은 이름의 첨부 파일을 덮어씁니다.")
    parser.add_argument(
        "--skip-existing",
        action="store_true",
        help="Already-imported posts are left unchanged. Useful for automatic batch imports.",
    )
    parser.add_argument(
        "--allow-empty",
        action="store_true",
        help="With --all, succeed without doing anything when imports/ has no ZIP files.",
    )
    parser.add_argument("--dry-run", action="store_true", help="파일을 만들지 않고 작업 결과만 표시합니다.")
    parser.add_argument("--content-root", type=Path, default=PROJECT_ROOT / "src" / "content" / "posts", help=argparse.SUPPRESS)
    parser.add_argument("--public-root", type=Path, default=PROJECT_ROOT / "public", help=argparse.SUPPRESS)
    return parser.parse_args()


def validate_args(args: argparse.Namespace) -> None:
    if args.all:
        if args.zip_path or args.slug or args.source:
            raise ImportErrorWithHint("--all은 ZIP 경로, --slug, --source와 함께 사용할 수 없습니다.")
        if not args.imports_dir.is_dir() and not args.allow_empty:
            raise ImportErrorWithHint(f"ZIP 폴더를 찾을 수 없습니다: {args.imports_dir}")
        if args.imports_dir.is_dir() and not any(args.imports_dir.glob("*.zip")) and not args.allow_empty:
            raise ImportErrorWithHint(f"ZIP 파일을 찾지 못했습니다: {args.imports_dir}")
        return

    if not args.zip_path:
        raise ImportErrorWithHint("ZIP 파일을 지정하거나 --all을 사용하세요.")
    if not args.zip_path.is_file():
        raise ImportErrorWithHint(f"ZIP 파일을 찾을 수 없습니다: {args.zip_path}")
    if args.zip_path.suffix.lower() != ".zip":
        raise ImportErrorWithHint("Notion에서 내려받은 .zip 파일을 지정하세요.")
    if not args.slug or not SLUG_RE.fullmatch(args.slug):
        raise ImportErrorWithHint("--slug는 소문자 영문·숫자·하이픈만 사용할 수 있습니다. 예: java-basic-syntax")


def extract_zip_safely(zip_path: Path, destination: Path) -> Path:
    """Extract without allowing a ZIP entry to escape the temporary directory."""
    destination_resolved = destination.resolve()
    with zipfile.ZipFile(zip_path) as archive:
        for info in archive.infolist():
            path = PurePosixPath(info.filename)
            if path.is_absolute() or ".." in path.parts:
                raise ImportErrorWithHint(f"안전하지 않은 ZIP 경로가 포함되어 있습니다: {info.filename}")
            if not path.parts or path.parts[0] == "__MACOSX":
                continue

            output = destination.joinpath(*path.parts)
            try:
                output.resolve().relative_to(destination_resolved)
            except ValueError as error:
                raise ImportErrorWithHint(f"안전하지 않은 ZIP 경로가 포함되어 있습니다: {info.filename}") from error

            if info.is_dir():
                output.mkdir(parents=True, exist_ok=True)
                continue
            output.parent.mkdir(parents=True, exist_ok=True)
            with archive.open(info) as source, output.open("wb") as target:
                shutil.copyfileobj(source, target)

    markdown_files = list(destination.rglob("*.md"))
    nested_archives = list(destination.glob("*.zip"))
    # Notion occasionally downloads an ExportBlock ZIP that contains only its
    # actual "Part-1" ZIP. Unwrap that container transparently.
    if not markdown_files and len(nested_archives) == 1:
        nested_archive = nested_archives[0]
        nested_destination = destination / "notion-export"
        try:
            return extract_zip_safely(nested_archive, nested_destination)
        except zipfile.BadZipFile:
            pass
    return destination


def select_source_markdown(extracted_root: Path, requested_source: str | None) -> Path:
    markdown_files = sorted(
        path for path in extracted_root.rglob("*.md") if "__MACOSX" not in path.parts
    )
    if not markdown_files:
        raise ImportErrorWithHint("ZIP 안에서 Markdown(.md) 파일을 찾지 못했습니다.")

    if requested_source:
        requested = extracted_root.joinpath(*PurePosixPath(requested_source).parts)
        if requested.is_file() and requested.suffix.lower() == ".md":
            return requested
        available = "\n".join(f"  - {path.relative_to(extracted_root).as_posix()}" for path in markdown_files)
        raise ImportErrorWithHint(f"--source 파일을 찾지 못했습니다: {requested_source}\n사용 가능한 파일:\n{available}")

    shallowest_depth = min(len(path.relative_to(extracted_root).parts) for path in markdown_files)
    candidates = [
        path for path in markdown_files
        if len(path.relative_to(extracted_root).parts) == shallowest_depth
    ]
    if len(candidates) == 1:
        return candidates[0]

    available = "\n".join(f"  - {path.relative_to(extracted_root).as_posix()}" for path in markdown_files)
    raise ImportErrorWithHint(
        "ZIP 안에 최상위 Markdown 파일이 여러 개입니다. 가져올 페이지를 --source로 지정하세요.\n"
        f"사용 가능한 파일:\n{available}"
    )


def parse_published_at(value: str) -> str | None:
    for pattern in (KOREAN_DATE_RE, ISO_DATE_RE):
        match = pattern.search(value)
        if not match:
            continue
        try:
            return date(
                int(match.group("year")),
                int(match.group("month")),
                int(match.group("day")),
            ).isoformat()
        except ValueError:
            return None
    return None


def opening_fence(line: str) -> tuple[str, int] | None:
    """Return a Markdown code-fence marker when a line opens one."""
    match = FENCE_OPEN_RE.match(line)
    if not match:
        return None
    marker = match.group("marker")
    return marker[0], len(marker)


def closes_fence(line: str, fence: tuple[str, int]) -> bool:
    """Return whether line closes the given CommonMark fenced code block."""
    marker, minimum_length = fence
    return bool(
        re.fullmatch(
            rf"[ \t]{{0,3}}{re.escape(marker)}{{{minimum_length},}}[ \t]*",
            line,
        )
    )


def extract_title_published_at_and_body(source_markdown: Path) -> tuple[str, str, str]:
    text = source_markdown.read_text(encoding="utf-8-sig")
    text = FRONTMATTER_RE.sub("", text, count=1).replace("\r\n", "\n")
    lines = text.split("\n")

    title = ""
    first_h1_index: int | None = None
    fence: tuple[str, int] | None = None
    for index, line in enumerate(lines):
        if fence:
            if closes_fence(line, fence):
                fence = None
            continue
        if opened_fence := opening_fence(line):
            fence = opened_fence
            continue
        match = H1_RE.match(line)
        if match:
            title = match.group("title").strip()
            first_h1_index = index
            break
    if not title:
        title = re.sub(r"\s+[0-9a-f]{32}$", "", source_markdown.stem, flags=re.IGNORECASE).strip()

    published_at: str | None = None
    normalized: list[str] = []
    fence = None
    for index, line in enumerate(lines):
        if fence:
            normalized.append(line)
            if closes_fence(line, fence):
                fence = None
            continue
        if opened_fence := opening_fence(line):
            normalized.append(line)
            fence = opened_fence
            continue
        match = H1_RE.match(line)
        if index == first_h1_index:
            continue
        date_match = DATE_METADATA_RE.match(line.strip())
        if date_match:
            parsed_date = parse_published_at(date_match.group("value"))
            if parsed_date:
                published_at = published_at or parsed_date
                continue
        if match:
            # BaseLayout already renders the post title as an h1.
            normalized.append(f"## {match.group('title')}")
        else:
            normalized.append(line)
    body = "\n".join(normalized).strip() + "\n"
    if not published_at:
        raise ImportErrorWithHint(
            "Notion Markdown 본문에서 `날짜: YYYY년 M월 D일` 또는 `날짜: YYYY-MM-DD` 형식을 찾지 못했습니다."
        )
    return title, published_at, body


def split_target(target: str) -> tuple[str, bool]:
    if target.startswith("<") and target.endswith(">"):
        return target[1:-1], True
    return target, False


def is_local_file_target(target: str) -> bool:
    parsed = urlsplit(target)
    return not (parsed.scheme or parsed.netloc or target.startswith(("/", "#")))


def resolve_local_target(source_markdown: Path, target: str, extracted_root: Path) -> Path | None:
    parsed = urlsplit(target)
    if not is_local_file_target(target) or not parsed.path:
        return None
    candidate = (source_markdown.parent / unquote(parsed.path)).resolve()
    try:
        candidate.relative_to(extracted_root.resolve())
    except ValueError:
        return None
    return candidate if candidate.is_file() else None


def destination_asset_path(asset: Path, source_markdown: Path, extracted_root: Path, public_root: Path, slug: str) -> Path:
    page_assets_directory = source_markdown.with_suffix("")
    try:
        relative_asset = asset.relative_to(page_assets_directory)
    except ValueError:
        relative_asset = asset.relative_to(extracted_root)
    folder = "images" if asset.suffix.lower() in IMAGE_EXTENSIONS else "files"
    return public_root / folder / slug / relative_asset


def public_url_for_asset(destination: Path, public_root: Path) -> str:
    relative = destination.relative_to(public_root).as_posix()
    return "/" + quote(relative, safe="/-._~")


def matching_inline_code_delimiter(text: str, start: int, length: int) -> tuple[int, int] | None:
    """Find a matching backtick run for an inline Markdown code span."""
    search_from = start
    while search_from < len(text):
        candidate_start = text.find("`", search_from)
        if candidate_start == -1:
            return None
        candidate_end = candidate_start
        while candidate_end < len(text) and text[candidate_end] == "`":
            candidate_end += 1
        if candidate_end - candidate_start == length:
            return candidate_start, candidate_end
        search_from = candidate_end
    return None


def rewrite_inline_code_free_text(text: str, rewrite: Callable[[str], str]) -> str:
    """Apply rewrite only outside inline Markdown code spans."""
    rewritten: list[str] = []
    plain_start = 0
    position = 0
    while position < len(text):
        opener_start = text.find("`", position)
        if opener_start == -1:
            break
        opener_end = opener_start
        while opener_end < len(text) and text[opener_end] == "`":
            opener_end += 1
        closer = matching_inline_code_delimiter(text, opener_end, opener_end - opener_start)
        if closer is None:
            # An unmatched delimiter is literal text, not a code span.
            position = opener_end
            continue
        closer_start, closer_end = closer
        rewritten.append(rewrite(text[plain_start:opener_start]))
        rewritten.append(text[opener_start:closer_end])
        plain_start = closer_end
        position = closer_end
    rewritten.append(rewrite(text[plain_start:]))
    return "".join(rewritten)


def rewrite_code_free_markdown(body: str, rewrite: Callable[[str], str]) -> str:
    """Apply rewrite outside fenced and inline Markdown code blocks."""
    rewritten: list[str] = []
    plain_lines: list[str] = []
    fence: tuple[str, int] | None = None

    def flush_plain_lines() -> None:
        if plain_lines:
            rewritten.append(rewrite_inline_code_free_text("".join(plain_lines), rewrite))
            plain_lines.clear()

    for line in body.splitlines(keepends=True):
        fence_line = line.rstrip("\r\n")
        if fence:
            rewritten.append(line)
            if closes_fence(fence_line, fence):
                fence = None
            continue
        if opened_fence := opening_fence(fence_line):
            flush_plain_lines()
            rewritten.append(line)
            fence = opened_fence
            continue
        plain_lines.append(line)
    flush_plain_lines()
    return "".join(rewritten)


def rewrite_links_and_collect_assets(
    body: str,
    source_markdown: Path,
    extracted_root: Path,
    public_root: Path,
    slug: str,
) -> tuple[str, list[tuple[Path, Path]], list[str]]:
    assets: dict[Path, Path] = {}
    warnings: list[str] = []

    def replace_link(match: re.Match[str]) -> str:
        raw_target, was_wrapped = split_target(match.group("target"))
        asset = resolve_local_target(source_markdown, raw_target, extracted_root)
        if asset is None:
            return match.group(0)
        if asset.suffix.lower() == ".md":
            warnings.append(
                f"하위 Notion 페이지 링크는 자동 변환하지 않았습니다: {raw_target}"
            )
            return match.group(0)

        destination = destination_asset_path(asset, source_markdown, extracted_root, public_root, slug)
        assets[asset] = destination
        parsed = urlsplit(raw_target)
        public_url = public_url_for_asset(destination, public_root)
        rewritten_target = urlunsplit(("", "", public_url, parsed.query, parsed.fragment))
        if was_wrapped:
            rewritten_target = f"<{rewritten_target}>"
        return f"{match.group('prefix')}[{match.group('label')}]({rewritten_target}{match.group('link_title') or ''})"

    rewritten = rewrite_code_free_markdown(
        body,
        lambda text: MARKDOWN_LINK_RE.sub(replace_link, text),
    )
    return rewritten, sorted(assets.items(), key=lambda pair: str(pair[1])), list(dict.fromkeys(warnings))


def build_frontmatter(title: str, published_at: str) -> str:
    return "\n".join(
        [
            "---",
            f"title: {json.dumps(title, ensure_ascii=False)}",
            f"publishedAt: {published_at}",
            "---",
            "",
        ]
    )


def notion_page_id(source_markdown: Path) -> str | None:
    """Return the stable Notion page ID embedded in an exported Markdown filename."""
    source_id = NOTION_ID_RE.search(source_markdown.stem)
    return source_id.group("id").lower() if source_id else None


def import_source_id(source_markdown: Path, zip_path: Path) -> str:
    """Return an identifier that remains stable across repeated exports of a page."""
    if page_id := notion_page_id(source_markdown):
        return f"notion-page-{page_id}"

    # Older or manually renamed exports may not expose the page ID. Retain the
    # previous ZIP-based fallback so those files can still be imported.
    zip_id = UUID_RE.search(zip_path.stem)
    if zip_id:
        return f"notion-export-{zip_id.group('id').replace('-', '').lower()}"
    digest = hashlib.sha256()
    with zip_path.open("rb") as archive_file:
        for chunk in iter(lambda: archive_file.read(1024 * 1024), b""):
            digest.update(chunk)
    return f"notion-export-sha256-{digest.hexdigest()}"


def import_source_marker(source_id: str) -> str:
    return f"<!-- notion-import-source: {source_id} -->"


def source_ids_in_posts(content_root: Path) -> set[str]:
    if not content_root.is_dir():
        return set()
    source_ids: set[str] = set()
    for post_path in content_root.glob("*.md"):
        text = post_path.read_text(encoding="utf-8-sig")
        source_ids.update(match.group("source_id") for match in IMPORT_SOURCE_MARKER_RE.finditer(text))
    return source_ids


def add_source_marker_to_existing_post(plan: ImportPlan) -> bool:
    """Migrate an older auto-named post so a later rename remains recognizable."""
    if not plan.post_path.is_file():
        return False
    text = plan.post_path.read_text(encoding="utf-8-sig")
    if IMPORT_SOURCE_MARKER_RE.search(text):
        return False
    frontmatter = FRONTMATTER_RE.match(text)
    if not frontmatter:
        return False
    updated = (
        text[:frontmatter.end()]
        + import_source_marker(plan.source_id)
        + "\n\n"
        + text[frontmatter.end():]
    )
    plan.post_path.write_text(updated, encoding="utf-8", newline="\n")
    return True


def auto_slug(source_markdown: Path, zip_path: Path) -> str:
    """Create a stable, collision-resistant slug for unattended batch imports."""
    if page_id := notion_page_id(source_markdown):
        return f"notion-{page_id[:8]}"

    # Fallback for exports whose Markdown file was manually renamed.
    zip_id = UUID_RE.search(zip_path.stem)
    if zip_id:
        return f"notion-{zip_id.group('id').replace('-', '')[:8].lower()}"
    raise ImportErrorWithHint(
        f"자동 slug를 만들 Notion ID를 찾지 못했습니다: {zip_path.name}. 개별 가져오기로 --slug를 지정하세요."
    )


def existing_post_for_source(content_root: Path, source_id: str) -> Path | None:
    """Find a renamed post by its stable import marker."""
    matches: list[Path] = []
    if content_root.is_dir():
        for post_path in content_root.glob("*.md"):
            text = post_path.read_text(encoding="utf-8-sig")
            if source_id in (
                match.group("source_id")
                for match in IMPORT_SOURCE_MARKER_RE.finditer(text)
            ):
                matches.append(post_path)
    if len(matches) > 1:
        paths = "\n".join(f"  - {path}" for path in matches)
        raise ImportErrorWithHint(
            "같은 Notion 페이지 ID를 가진 기존 글이 여러 개라서 덮어쓸 글을 결정할 수 없습니다.\n"
            f"중복 글:\n{paths}"
        )
    return matches[0] if matches else None


def frontmatter_title(post_path: Path) -> str | None:
    """Read the JSON-compatible title emitted by this importer."""
    text = post_path.read_text(encoding="utf-8-sig")
    frontmatter = FRONTMATTER_RE.match(text)
    if not frontmatter:
        return None
    for line in frontmatter.group(0).splitlines():
        if not line.startswith("title:"):
            continue
        try:
            title = json.loads(line.removeprefix("title:").strip())
        except json.JSONDecodeError:
            return None
        return title if isinstance(title, str) else None
    return None


def legacy_post_for_title(content_root: Path, title: str) -> Path | None:
    """Find the one legacy ZIP-identified post that can be migrated safely."""
    matches: list[Path] = []
    if content_root.is_dir():
        for post_path in content_root.glob("*.md"):
            text = post_path.read_text(encoding="utf-8-sig")
            source_ids = {
                match.group("source_id")
                for match in IMPORT_SOURCE_MARKER_RE.finditer(text)
            }
            if (
                any(source_id.startswith("notion-export-") for source_id in source_ids)
                and frontmatter_title(post_path) == title
            ):
                matches.append(post_path)
    if len(matches) > 1:
        paths = "\n".join(f"  - {path}" for path in matches)
        raise ImportErrorWithHint(
            f"제목이 `{title}`인 기존 글이 여러 개라서 자동으로 합칠 수 없습니다.\n"
            f"중복 글:\n{paths}"
        )
    return matches[0] if matches else None


def create_import_plan(args: argparse.Namespace, zip_path: Path, slug: str | None = None) -> ImportPlan:
    with tempfile.TemporaryDirectory(prefix="notion-export-") as temporary_directory:
        extracted_root = extract_zip_safely(zip_path, Path(temporary_directory))
        source_markdown = select_source_markdown(extracted_root, args.source)
        title, published_at, body = extract_title_published_at_and_body(source_markdown)
        source_id = import_source_id(source_markdown, zip_path)
        resolved_slug = slug or auto_slug(source_markdown, zip_path)
        if slug is None:
            existing_post = existing_post_for_source(args.content_root, source_id)
            natural_post = args.content_root / f"{resolved_slug}.md"
            if not existing_post and not natural_post.exists():
                existing_post = legacy_post_for_title(args.content_root, title)
            if existing_post:
                resolved_slug = existing_post.stem
        rewritten_body, assets, warnings = rewrite_links_and_collect_assets(
            body, source_markdown, extracted_root, args.public_root, resolved_slug
        )
        copied_assets = [
            AssetCopy(source.relative_to(extracted_root), destination)
            for source, destination in assets
        ]
        post_path = args.content_root / f"{resolved_slug}.md"
        plan = ImportPlan(
            zip_path=zip_path,
            source_markdown=source_markdown,
            post_path=post_path,
            title=title,
            published_at=published_at,
            source_id=source_id,
            body=(
                build_frontmatter(title, published_at)
                + import_source_marker(source_id)
                + "\n\n"
                + rewritten_body
            ),
            copied_assets=copied_assets,
            warnings=warnings,
        )
        return plan


def ensure_plans_are_writable(plans: list[ImportPlan], overwrite: bool) -> None:
    destinations: dict[Path, Path] = {}
    duplicate_destinations: list[Path] = []
    for plan in plans:
        for destination in [plan.post_path, *(asset.destination for asset in plan.copied_assets)]:
            if destination in destinations:
                duplicate_destinations.append(destination)
            destinations[destination] = plan.zip_path
    if duplicate_destinations:
        paths = "\n".join(f"  - {path}" for path in sorted(set(duplicate_destinations)))
        raise ImportErrorWithHint(
            "가져올 ZIP들이 같은 파일을 만들려고 합니다. 중복 내보내기를 imports/에서 빼거나 개별 가져오기를 사용하세요.\n"
            f"충돌 경로:\n{paths}"
        )

    collisions = [path for path in destinations if path.exists()]
    if collisions and not overwrite:
        paths = "\n".join(f"  - {path}" for path in collisions)
        raise ImportErrorWithHint(
            "같은 경로에 이미 파일이 있습니다. slug를 바꾸거나 --overwrite를 사용하세요.\n"
            f"충돌 경로:\n{paths}"
        )


def deduplicate_plans(plans: list[ImportPlan]) -> tuple[list[ImportPlan], list[ImportPlan]]:
    """Keep only the newest export when the same Notion page appears repeatedly."""
    unique_by_post_path: dict[Path, ImportPlan] = {}
    duplicates: list[ImportPlan] = []
    for plan in plans:
        existing = unique_by_post_path.get(plan.post_path)
        if existing is None:
            unique_by_post_path[plan.post_path] = plan
            continue

        if existing.source_id != plan.source_id:
            raise ImportErrorWithHint(
                "서로 다른 Notion 페이지가 같은 글 경로를 사용하려고 합니다.\n"
                f"충돌 ZIP:\n  - {existing.zip_path.name}\n  - {plan.zip_path.name}"
            )

        existing_order = (existing.zip_path.stat().st_mtime_ns, existing.zip_path.name)
        current_order = (plan.zip_path.stat().st_mtime_ns, plan.zip_path.name)
        if current_order > existing_order:
            duplicates.append(existing)
            unique_by_post_path[plan.post_path] = plan
        else:
            duplicates.append(plan)
    return list(unique_by_post_path.values()), duplicates


def write_plan(plan: ImportPlan) -> None:
    plan.post_path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="notion-export-write-") as temporary_directory:
        extracted_root = extract_zip_safely(plan.zip_path, Path(temporary_directory))
        for asset in plan.copied_assets:
            source = extracted_root / asset.source_relative_path
            if not source.is_file():
                raise ImportErrorWithHint(
                    f"가져오기 중 첨부 파일을 다시 찾지 못했습니다: {asset.source_relative_path}"
                )
            asset.destination.parent.mkdir(parents=True, exist_ok=True)
            with source.open("rb") as source_file, asset.destination.open("wb") as destination_file:
                shutil.copyfileobj(source_file, destination_file)
    plan.post_path.write_text(plan.body, encoding="utf-8", newline="\n")


def main() -> int:
    args = parse_args()
    try:
        validate_args(args)
        if args.all:
            zip_paths = sorted(args.imports_dir.glob("*.zip")) if args.imports_dir.is_dir() else []
            if not zip_paths:
                print("No Notion export ZIP files found; skipping import.")
                return 0
            plans = [create_import_plan(args, zip_path) for zip_path in zip_paths]
            plans, duplicates = deduplicate_plans(plans)
        else:
            plans = [create_import_plan(args, args.zip_path, args.slug)]
            duplicates = []
        skipped = []
        marked = []
        if args.skip_existing:
            if not args.dry_run:
                marked = [plan for plan in plans if add_source_marker_to_existing_post(plan)]
            existing_source_ids = source_ids_in_posts(args.content_root)
            skipped = [
                plan
                for plan in plans
                if plan.post_path.exists() or plan.source_id in existing_source_ids
            ]
            plans = [plan for plan in plans if plan not in skipped]
        ensure_plans_are_writable(plans, args.overwrite)
        if not args.dry_run:
            for plan in plans:
                write_plan(plan)
    except (ImportErrorWithHint, zipfile.BadZipFile, UnicodeDecodeError) as error:
        print(f"가져오지 못했습니다: {error}", file=sys.stderr)
        return 1

    action = "미리보기" if args.dry_run else "가져오기 완료"
    print(f"{action}: {len(plans)}개 글")
    for plan in plans:
        print(f"- {plan.title} ({plan.published_at}) → {plan.post_path}")
        print(f"  첨부 파일: {len(plan.copied_assets)}개")
        for warning in plan.warnings:
            print(f"  경고: {warning}")
    for duplicate in duplicates:
        print(f"중복 제외: {duplicate.zip_path.name}")
    for marked_plan in marked:
        print(f"Added import marker: {marked_plan.post_path.name}")
    for skipped_plan in skipped:
        print(f"Skipped existing post: {skipped_plan.post_path.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
