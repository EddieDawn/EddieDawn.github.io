---
title: "SW문제해결응용 - 그래프응용"
publishedAt: 2026-09-10
---
<!-- notion-import-source: notion-page-3d8154b95f678012865ad03d8a67ed77 -->

## 위상정렬 (Topological Sort)

순서가 있는 작업들의 작업 순서를 정함
먼저 / 나중 관계만 지키는 줄 세우기
→ 정답이 여러개일 수 있음

## 사전지식

- DAG (Directed Acyclic Graph)
    
    사이클이 없는 유향 그래프
    

위상 정렬은 DAG에서만 가능해요

![image.png](/images/SW%EB%AC%B8%EC%A0%9C%ED%95%B4%EA%B2%B0%EC%9D%91%EC%9A%A9%20-%20%EA%B7%B8%EB%9E%98%ED%94%84%EC%9D%91%EC%9A%A9/image.png)

- 진입 차수
    
    특정 노드로 들어오는 간선의 개수
    
- 진출 차수
    
    특정 노드에서 나가는 간선의 개수
    

→ 위상정렬에서는 진입 차수만 신경쓰기

진입 차수가 0인 애들만 작업 시작 가능

![image.png](/images/SW%EB%AC%B8%EC%A0%9C%ED%95%B4%EA%B2%B0%EC%9D%91%EC%9A%A9%20-%20%EA%B7%B8%EB%9E%98%ED%94%84%EC%9D%91%EC%9A%A9/image%201.png)

![image.png](/images/SW%EB%AC%B8%EC%A0%9C%ED%95%B4%EA%B2%B0%EC%9D%91%EC%9A%A9%20-%20%EA%B7%B8%EB%9E%98%ED%94%84%EC%9D%91%EC%9A%A9/image%202.png)

## 위상정렬 Queue 구현

1. 진입 차수가 0인 모든 노드를 Queue에 삽입
2. while (!q.isEmpty)
    1.
