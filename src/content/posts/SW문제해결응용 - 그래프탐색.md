---
title: "SW문제해결응용 - 그래프탐색"
publishedAt: 2026-09-09
---
<!-- notion-import-source: notion-page-3d6154b95f67808f92adc1c48434003a -->

## 그래프 기본

정점(vertex)와 간선(edge)로 이어져 있는 연결 관계를 나타낸 자료

- vertex (or node)
    
    : 데이터 포인트
    
- edge
    
    : 정점과 정점 간의 관계 설명
    
- adjacent
    
    : 두 vertex가 edge로 이어져 있을 때 adjacent(인접)해 있다고 한다.
    
- degree
    
    : 하나의 vertex에 연결되어 있는 간선의 개수
    

![image.png](/images/SW%EB%AC%B8%EC%A0%9C%ED%95%B4%EA%B2%B0%EC%9D%91%EC%9A%A9%20-%20%EA%B7%B8%EB%9E%98%ED%94%84%ED%83%90%EC%83%89/image.png)

## 그래프의 종류

- Undiredted
- Diredted
- Weighted
- Cyclic
- DAG

## 그래프 표현 방법

→ 코테에서 그래프 문제 나오면 어떻게 구현할래?

![그래프가 이렇게 생겼다 칩시다](/images/SW%EB%AC%B8%EC%A0%9C%ED%95%B4%EA%B2%B0%EC%9D%91%EC%9A%A9%20-%20%EA%B7%B8%EB%9E%98%ED%94%84%ED%83%90%EC%83%89/image%201.png)

그래프가 이렇게 생겼다 칩시다

## 1. Adjacent Matrix

간선의 유무를 N x N 2차원 배열로 표현한다

![image.png](/images/SW%EB%AC%B8%EC%A0%9C%ED%95%B4%EA%B2%B0%EC%9D%91%EC%9A%A9%20-%20%EA%B7%B8%EB%9E%98%ED%94%84%ED%83%90%EC%83%89/image%202.png)

![image.png](/images/SW%EB%AC%B8%EC%A0%9C%ED%95%B4%EA%B2%B0%EC%9D%91%EC%9A%A9%20-%20%EA%B7%B8%EB%9E%98%ED%94%84%ED%83%90%EC%83%89/image%203.png)

## 2. Adjacent List

각 정점에 대한 인접 정점들만 순서대로 모아 놓는다

![image.png](/images/SW%EB%AC%B8%EC%A0%9C%ED%95%B4%EA%B2%B0%EC%9D%91%EC%9A%A9%20-%20%EA%B7%B8%EB%9E%98%ED%94%84%ED%83%90%EC%83%89/image%204.png)

## 3. Edge Array

‘간선 배열’이라는걸 만들어서 두 정점의 정보를 배열 / 객체로 만든다.

![image.png](/images/SW%EB%AC%B8%EC%A0%9C%ED%95%B4%EA%B2%B0%EC%9D%91%EC%9A%A9%20-%20%EA%B7%B8%EB%9E%98%ED%94%84%ED%83%90%EC%83%89/image%205.png)

## 세 방법 총 비교

![image.png](/images/SW%EB%AC%B8%EC%A0%9C%ED%95%B4%EA%B2%B0%EC%9D%91%EC%9A%A9%20-%20%EA%B7%B8%EB%9E%98%ED%94%84%ED%83%90%EC%83%89/image%206.png)

## 그래프 탐색법

## BFS

Breadth First Search: 넓이 우선 탐색
시작 지점에서 가까운 곳부터 탐색한다. 즉, 거리가 1인 vertex인 곳을 모두 방문해야 거리 2인 vertex를 방문.

FIFO자료형인 Queue를 활용 (아직 가보지 않은, 다음에 가볼 곳)
모든 Edge의 비용이 같을 때, 시작 지점에서 목표 지점까지의 최단 거리를 구함

![image.png](/images/SW%EB%AC%B8%EC%A0%9C%ED%95%B4%EA%B2%B0%EC%9D%91%EC%9A%A9%20-%20%EA%B7%B8%EB%9E%98%ED%94%84%ED%83%90%EC%83%89/image%207.png)

근데 이러면 같은 정점을 계속 방문함. visited 배열이 있어야함

![image.png](/images/SW%EB%AC%B8%EC%A0%9C%ED%95%B4%EA%B2%B0%EC%9D%91%EC%9A%A9%20-%20%EA%B7%B8%EB%9E%98%ED%94%84%ED%83%90%EC%83%89/image%208.png)

!많이하는실수

![image.png](/images/SW%EB%AC%B8%EC%A0%9C%ED%95%B4%EA%B2%B0%EC%9D%91%EC%9A%A9%20-%20%EA%B7%B8%EB%9E%98%ED%94%84%ED%83%90%EC%83%89/image%209.png)

## DFS

Depth First Search : 깊이 우선 탐색
진행할 수 없다면 마지막에 만난 지점으로 돌아와 다른 방향 다시 탐색
LIFO 구조의 스택(stack) 사용

### 재귀로 구현하기

### stack으로 구현하기
