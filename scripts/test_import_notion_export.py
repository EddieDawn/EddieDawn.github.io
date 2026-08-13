#!/usr/bin/env python3
"""End-to-end test for the Notion ZIP importer using only temporary files."""

from __future__ import annotations

import subprocess
import sys
import tempfile
import zipfile
from io import BytesIO
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
IMPORTER = PROJECT_ROOT / "scripts" / "import_notion_export.py"


def main() -> int:
    with tempfile.TemporaryDirectory(prefix="notion-import-test-") as temporary_directory:
        root = Path(temporary_directory)
        archive = root / "export.zip"
        inner_archive = BytesIO()
        with zipfile.ZipFile(inner_archive, "w") as exported:
            exported.writestr(
                "Java basic.md",
                "# Java 기본 문법\n\n"
                "날짜: 2026년 8월 13일\n\n"
                "[공식 문서](https://docs.oracle.com/)와 [첨부](Java%20basic/guide.pdf)를 참고한다.\n\n"
                "인라인 예시: `[첨부 예시](Java%20basic/example.pdf)`\n\n"
                "![실행 흐름](Java%20basic/flow.png)\n\n"
                "# 변수\n\n```md\n# 코드 안의 제목\ndate: 2026-08-13\n[첨부 예시](Java%20basic/example.pdf)\n```\n",
            )
            exported.writestr("Java basic/flow.png", b"test-image")
            exported.writestr("Java basic/guide.pdf", b"test-pdf")
            exported.writestr("Java basic/example.pdf", b"example-only-pdf")
        with zipfile.ZipFile(archive, "w") as wrapped_export:
            wrapped_export.writestr("ExportBlock-example-Part-1.zip", inner_archive.getvalue())

        content_root = root / "content"
        public_root = root / "public"
        result = subprocess.run(
            [
                sys.executable,
                str(IMPORTER),
                str(archive),
                "--slug", "java-basic",
                "--content-root", str(content_root),
                "--public-root", str(public_root),
            ],
            text=True,
            capture_output=True,
            check=False,
        )
        if result.returncode:
            print(result.stderr, file=sys.stderr)
            return result.returncode

        post = (content_root / "java-basic.md").read_text(encoding="utf-8")
        assert 'title: "Java 기본 문법"' in post
        assert "publishedAt: 2026-08-13" in post
        assert "<!-- notion-import-source: notion-export-sha256-" in post
        assert "description:" not in post
        assert "category:" not in post
        assert "tags:" not in post
        assert "draft:" not in post
        assert "날짜: 2026년 8월 13일" not in post
        assert "# Java 기본 문법" not in post
        assert "## 변수" in post
        assert "`[첨부 예시](Java%20basic/example.pdf)`" in post
        assert (
            "```md\n# 코드 안의 제목\ndate: 2026-08-13\n"
            "[첨부 예시](Java%20basic/example.pdf)\n```"
        ) in post
        assert "](/images/java-basic/flow.png)" in post
        assert "](/files/java-basic/guide.pdf)" in post
        assert (public_root / "images" / "java-basic" / "flow.png").read_bytes() == b"test-image"
        assert (public_root / "files" / "java-basic" / "guide.pdf").read_bytes() == b"test-pdf"
        assert not (public_root / "files" / "java-basic" / "example.pdf").exists()

        batch_imports = root / "imports"
        batch_imports.mkdir()
        for filename, title, day, identifier in [
            ("11111111-1111-1111-1111-111111111111_ExportBlock.zip", "첫 번째 글", "2026년 8월 14일", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"),
            ("22222222-2222-2222-2222-222222222222_ExportBlock.zip", "두 번째 글", "2026년 8월 15일", "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"),
        ]:
            with zipfile.ZipFile(batch_imports / filename, "w") as exported:
                exported.writestr(
                    f"{title} {identifier}.md",
                    f"# {title}\n\n날짜: {day}\n\n본문\n",
                )
        batch_content_root = root / "batch-content"
        batch_result = subprocess.run(
            [
                sys.executable,
                str(IMPORTER),
                "--all",
                "--imports-dir", str(batch_imports),
                "--content-root", str(batch_content_root),
                "--public-root", str(root / "batch-public"),
            ],
            text=True,
            capture_output=True,
            check=False,
        )
        if batch_result.returncode:
            print(batch_result.stderr, file=sys.stderr)
            return batch_result.returncode
        assert (batch_content_root / "notion-11111111.md").is_file()
        assert (batch_content_root / "notion-22222222.md").is_file()
        renamed_post = batch_content_root / "friendly-first-post.md"
        (batch_content_root / "notion-11111111.md").rename(renamed_post)
        repeat_batch_result = subprocess.run(
            [
                sys.executable,
                str(IMPORTER),
                "--all",
                "--skip-existing",
                "--imports-dir", str(batch_imports),
                "--content-root", str(batch_content_root),
                "--public-root", str(root / "batch-public"),
            ],
            text=True,
            capture_output=True,
            check=False,
        )
        if repeat_batch_result.returncode:
            print(repeat_batch_result.stderr, file=sys.stderr)
            return repeat_batch_result.returncode
        assert renamed_post.is_file()
        assert not (batch_content_root / "notion-11111111.md").exists()

    print("Notion ZIP importer test passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
