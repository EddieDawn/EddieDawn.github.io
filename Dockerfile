# Node.js 24은 현재 장기 지원(LTS) 버전입니다.
FROM node:24-bookworm

# 컨테이너 안에서 프로젝트를 작업할 기본 폴더입니다.
WORKDIR /workspace

# 컨테이너 안에서도 Git 명령과 Notion 가져오기 스크립트를 사용할 수 있도록 설치합니다.
RUN apt-get update \
    && apt-get install --yes --no-install-recommends git python3 \
    && rm -rf /var/lib/apt/lists/*

# VS Code가 접속할 때까지 컨테이너가 종료되지 않도록 유지합니다.
CMD ["sleep", "infinity"]
