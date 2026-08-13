---
title: "1. GIT"
publishedAt: 2026-07-20
---
<!-- notion-import-source: notion-export-a85b545a311c4df2a2b656a1eab6bbed -->

## GIT이란?

버전 관리자인데 분산형임

협업할때 코드 안 꼬이게 도와줌

## 명령어

```powershell
git init
```

내 working directory를 git이 감시 시작하도록 하는 명령어

```powershell
git config --global user.name
git config --global user.email
```

![working directory, staging area, local repo, remote repo의 관계](/images/notion-a85b545a/image.png)

working directory, staging area, local repo, remote repo의 관계

git은 변경사항을 올릴라면 내 정보가 필요하다. 누가 수정했는지 남겨야 하니까.

```powershell
git status
```

뭐가 변경되었고 스테이지 되었고 알려줌

```powershell
git add (filename)
```

특정 파일을 staging한다. git add . 는 하위 디렉토리에 포함된거 싹다 올림

```powershell
git commit -m (커밋메시지)
```

stage된 변경사항을 commit하기

## 실습하기

내 고양이 도리 소개 페이지 만들기

[code_artifact.zip](/files/notion-a85b545a/code_artifact.zip)

[code_artifact_2.zip](/files/notion-a85b545a/code_artifact_2.zip)

## Branch

## Merge

## Fast-forward

## Three-way

## Unit test

## .gitignore
