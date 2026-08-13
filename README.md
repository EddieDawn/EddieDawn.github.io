# Eddie's Dev Blog

> 배운 것을 기록하고, 기록을 통해 성장하는 개발 블로그

부트캠프 TIL과 개인 개발·스터디 경험을 정리하기 위해 만드는 개인 블로그입니다. 이 저장소는 단순한 블로그 결과물뿐 아니라 Docker, 개발환경 통일, 자동 배포까지 직접 학습하는 과정도 함께 담습니다.

## 목표

- Markdown으로 부담 없이 TIL과 기술 글을 작성한다.
- 읽기 쉬운 구조와 일관된 글 품질을 유지한다.
- 집과 부트캠프 등 어느 환경에서도 같은 개발환경을 사용한다.
- 비용 없이 GitHub Pages로 배포하고 운영한다.

## 현재 구성

| 구분 | 선택한 도구 | 역할 |
| --- | --- | --- |
| 개발환경 | Docker + Docker Compose | Node.js와 Git이 포함된 공통 Linux 개발환경 |
| 에디터 환경 | VS Code Dev Containers | 컨테이너 접속과 확장 프로그램 자동 설치 |
| 코드 품질 | ESLint + Prettier | 코드 검사 및 자동 포맷 |
| 글 작성 지원 | Markdownlint + Markdown All in One | Markdown 문법·형식 검사와 작성 편의 기능 |
| 설정 파일 지원 | YAML | Docker Compose와 GitHub Actions YAML 작성 지원 |

## 시작하기

### 준비물

- [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- [Visual Studio Code](https://code.visualstudio.com/)
- VS Code의 **Dev Containers** 확장 프로그램

### 개발 컨테이너 열기

1. Docker Desktop을 실행합니다.
2. VS Code에서 이 저장소 폴더를 엽니다.
3. `Ctrl + Shift + P`를 누르고 **Dev Containers: Rebuild and Reopen in Container**를 실행합니다.
4. 컨테이너 접속이 끝나면 VS Code 터미널에서 다음을 확인합니다.

   ```bash
   pwd
   node --version
   git --version
   ```

   `pwd`의 결과가 `/workspace`이면 정상입니다.

## Docker 명령어

프로젝트 루트에서 실행합니다.

```bash
# Dockerfile을 바탕으로 개발 이미지를 생성합니다.
docker compose build

# 개발 컨테이너를 백그라운드에서 실행합니다.
docker compose up -d

# 실행 중인 개발 컨테이너를 중지하고 제거합니다.
docker compose down
```

> 소스 코드는 내 컴퓨터의 프로젝트 폴더에 보관되고 컨테이너의 `/workspace`에 연결됩니다. 따라서 컨테이너를 제거해도 작성한 코드와 글은 사라지지 않습니다.

## 디렉터리 구조

```text
.
├── .devcontainer/
│   └── devcontainer.json  # VS Code 개발 컨테이너·확장 프로그램 설정
├── Dockerfile             # Node.js와 Git을 포함한 개발 이미지 설계도
├── compose.yaml           # 컨테이너 실행, 폴더·포트 연결 설정
└── README.md
```

## 앞으로 만들 기능

- [ ] Astro 기반 블로그 기본 구조
- [ ] Markdown 글 작성과 글 목록·상세 페이지
- [ ] 반응형 디자인과 가독성 개선
- [ ] GitHub Pages 자동 배포
- [ ] GitHub Actions 기반 빌드·배포 검증

---

Made with curiosity, consistency, and lots of notes.
