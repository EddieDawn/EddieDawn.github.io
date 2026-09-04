---
title: "SW문제해결기본 - Heap"
publishedAt: 2026-09-03
---
<!-- notion-import-source: notion-page-3d0154b95f6780df9b45fc682790dde5 -->

## Complete Binary Tree

모든 노드의 자식이 최대 2개이고, 마지막 레벨을 뺀 모든 레벨이 꽉 차있고, 마지막 레벨은 왼쪽부터 빈틈없이 채워친 트리

## Heap

우선순위 큐를 구현하는데 주로 사용됨. 전체 정렬 상태는 아니며 루트 값만 최대 / 최소값임이 보장됨.

## Max Heap

키 값이 가장 큰 노드를 찾기 위한 완전 이진 트리

![부모 노드의 값 ≥ 자식 노드의 값](/images/SW%EB%AC%B8%EC%A0%9C%ED%95%B4%EA%B2%B0%EA%B8%B0%EB%B3%B8%20-%20Heap/image.png)

부모 노드의 값 ≥ 자식 노드의 값

부모 - 자식 관계만 지키면 되고, 같은 레벨의 노드끼리는 크기 비교 x

## Min Heap

키 값이 가장 작은 노드를 찾기 위한 완전 이진 트리

![부모 노드의 값 ≤ 자식 노드의 값](/images/SW%EB%AC%B8%EC%A0%9C%ED%95%B4%EA%B2%B0%EA%B8%B0%EB%B3%B8%20-%20Heap/image%201.png)

부모 노드의 값 ≤ 자식 노드의 값

## 힙의 삽입 연산 ( O(log N) )

![image.png](/images/SW%EB%AC%B8%EC%A0%9C%ED%95%B4%EA%B2%B0%EA%B8%B0%EB%B3%B8%20-%20Heap/image%202.png)

![image.png](/images/SW%EB%AC%B8%EC%A0%9C%ED%95%B4%EA%B2%B0%EA%B8%B0%EB%B3%B8%20-%20Heap/image%203.png)

## 힙의 삭제 연산 ( O(log N) )

![image.png](/images/SW%EB%AC%B8%EC%A0%9C%ED%95%B4%EA%B2%B0%EA%B8%B0%EB%B3%B8%20-%20Heap/image%204.png)
