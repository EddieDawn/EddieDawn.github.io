# Eddie's TIL

> 배운 것을 Markdown으로 기록하고, GitHub Pages에 배포하는 개인 개발 학습 기록 사이트입니다.

글 파일을 추가하면 Astro가 최신 글 목록과 글 상세 페이지를 정적 HTML로 생성합니다.

## 현재 구현된 기능

- Astro + Tailwind CSS 기반의 반응형 정적 사이트
- 프로필 사이드바와 GitHub · Instagram · Email 링크
- Markdown 기반 글 작성 및 글 목록/상세 페이지 자동 생성
- 최신 발행일 순 글 정렬
- Docker Compose + VS Code Dev Containers 개발 환경
- GitHub Actions를 통한 PR 검사 및 GitHub Pages 배포

## 기술 구성

| 구분 | 기술 | 역할 |
| --- | --- | --- |
| 웹 프레임워크 | Astro | Markdown 글을 읽고 빠른 정적 페이지를 생성합니다. |
| 스타일 | Tailwind CSS | 화면의 색상, 여백, 반응형 레이아웃을 작성합니다. |
| 콘텐츠 | Astro Content Collections + Markdown | 글의 메타데이터를 검사하고 목록/상세 페이지에 제공합니다. |
| 개발 환경 | Docker Compose + Dev Containers | 누구나 같은 Node.js/Linux 환경에서 개발합니다. |
| 배포 | GitHub Actions + GitHub Pages | `main` 브랜치에 반영된 사이트를 자동 배포합니다. |

## 로컬 개발 시작하기

### 1. Docker 개발 컨테이너 열기

Docker Desktop을 실행한 뒤 VS Code로 저장소 폴더를 엽니다.

1. `Ctrl + Shift + P`
2. **Dev Containers: Rebuild and Reopen in Container** 선택
3. 컨테이너 터미널에서 아래 명령 실행

```bash
npm ci
npm run dev
```

브라우저에서 `http://localhost:4321`을 열면 사이트를 볼 수 있습니다. `--host 0.0.0.0` 설정이 되어 있어 Docker 컨테이너 밖의 브라우저에서도 접속할 수 있습니다.

### Docker 명령으로 직접 실행하기

VS Code Dev Container를 사용하지 않는 경우, 프로젝트 루트에서 실행합니다.

```bash
docker compose build
docker compose up -d
docker compose exec blog bash
```

컨테이너 안에서 `npm ci` 후 `npm run dev`를 실행합니다.

## 자주 사용하는 명령어

```bash
# 개발 서버 실행: 파일을 저장하면 화면이 자동으로 갱신됩니다.
npm run dev

# Astro/TypeScript 타입 및 문법 검사
npm run check

# GitHub Pages에 올릴 정적 파일을 dist/에 생성
npm run build

# build 결과물을 로컬에서 확인
npm run preview
```

## 새 글 작성하기

`src/content/posts/` 아래에 Markdown 파일을 추가합니다. 파일명은 URL slug가 됩니다. 예를 들어 `src/content/posts/array-list.md`는 `/posts/array-list/`에 표시됩니다.

```md
---
title: "ArrayList 정리"
publishedAt: 2026-08-13
---

## ArrayList

여기부터 본문을 Markdown으로 작성합니다.
```

글의 frontmatter에는 `title`, `publishedAt`만 작성합니다. 설명, 카테고리, 태그, 초안 상태는 사용하지 않습니다.

글을 추가하면 아래 주소가 자동으로 만들어집니다.

```text
/posts/array-list/
```

### Notion 글 가져오기

Notion의 글 페이지에서 **`•••` → `내보내기` → `Markdown & CSV`**를 선택해 ZIP 파일을 받습니다. ZIP 파일은 Git에 올리지 않도록 `imports/` 폴더에 두는 것을 권장합니다.

가져올 글의 URL slug만 정한 뒤 아래 명령을 실행합니다. 제목과 발행일은 Notion Markdown의 제목과 `날짜:` 줄에서 가져옵니다.

```bash
python3 scripts/import_notion_export.py imports/java-basic.zip \
  --slug java-basic-syntax
```

스크립트가 하는 일은 다음과 같습니다.

- `src/content/posts/<slug>.md`에 `title`, `publishedAt`만 담은 Astro frontmatter를 붙인 글을 생성합니다.
- Notion의 최상단 제목(`# 제목`)과 `날짜:` 줄은 frontmatter로 옮기고 본문에서는 제거합니다. 본문의 다른 `#` 제목은 `##`로 바꿉니다. 글 상세 페이지가 제목을 이미 `h1`으로 출력하기 때문입니다.
- ZIP 안의 이미지 링크는 `public/images/<slug>/`로 복사하고 `/images/<slug>/...` 경로로 변경합니다.
- PDF 등 첨부 파일 링크는 `public/files/<slug>/`로 복사하고 `/files/<slug>/...` 경로로 변경합니다.
- 외부 링크는 그대로 유지합니다.

동일한 slug가 이미 있으면 실수로 덮어쓰지 않고 멈춥니다. 다시 가져오려면 내용을 확인한 뒤 `--overwrite`를 붙입니다. ZIP에 여러 Markdown 페이지가 있으면 원하는 페이지를 `--source`로 지정합니다.

```bash
python3 scripts/import_notion_export.py imports/export.zip \
  --slug java-basic-syntax \
  --source "Java 기본 문법.md" \
  --overwrite
```

파일을 만들지 않고 결과만 확인하려면 `--dry-run`을 붙입니다. 스크립트 검증은 다음 명령으로 실행합니다.

```bash
python3 scripts/test_import_notion_export.py
```

`imports/`에 ZIP을 여러 개 넣었다면 아래 명령으로 한 번에 가져옵니다.

```bash
python3 scripts/import_notion_export.py --all
```

배치 가져오기는 ZIP 내부 Markdown 파일명에 포함된 Notion 페이지 ID로 `notion-<ID 앞 8자리>.md` 파일을 만듭니다. 같은 페이지를 다시 내보낸 ZIP은 ID가 유지되므로 기존 글과 첨부 파일을 덮어씁니다. 같은 페이지의 ZIP이 여러 개 남아 있으면 수정 시각이 가장 최신인 ZIP을 사용합니다. 제목을 정확한 영어 URL로 자동 번역할 수는 없기 때문에 충돌 없는 임시 slug를 사용하며, 원하면 가져온 뒤 파일명을 바꿔 URL을 정리할 수 있습니다.

## 프로젝트 구조

```text
src/
├── components/             # Header, Footer, ProfileSidebar, PostCard
├── config/                 # 사이트 정보 설정
├── content/
│   └── posts/              # 작성한 Markdown 글
├── content.config.ts       # posts 컬렉션의 위치와 글 형식(schema) 정의
├── layouts/                # 공통 페이지 레이아웃
├── pages/
│   ├── index.astro         # 최신 글 목록 랜딩 페이지
│   ├── posts.astro         # 전체 글 목록
│   ├── posts/[...slug].astro # Markdown 글 상세 페이지
└── styles/                 # 전역 스타일

.github/workflows/
├── ci.yml                  # PR 및 기능 브랜치 검사
└── main.yml                # main 브랜치 GitHub Pages 배포
```

## 배포 흐름

1. 기능 브랜치에서 작업하고 Pull Request를 만듭니다.
2. `ci.yml`이 `npm run check`, `npm run build`를 실행합니다.
3. PR을 `main`에 병합합니다.
4. `main.yml`이 `dist/`를 GitHub Pages에 배포합니다.

배포 전에는 로컬에서 다음 명령으로 같은 검사를 실행할 수 있습니다.

```bash
npm run check
npm run build
```

## 설정을 바꾸는 위치

| 바꾸고 싶은 내용 | 파일 |
| --- | --- |
| 이름, 소개, 프로필 링크 | `src/config/site.ts` |
| 글의 필수 항목 | `src/content.config.ts` |
| 전체 색상·폰트·Markdown 본문 스타일 | `src/styles/global.css` |

---

Made with curiosity, consistency, and lots of notes.
