---
title: "SW문제해결기본 - LinkedList"
publishedAt: 2026-09-02
---
<!-- notion-import-source: notion-page-3cf154b95f678015b941f7bb92218495 -->

## LinkedList

Node가 데이터와 다음 node의 주소를 가지는 방식으로 이어 붙인 자료구조
첫 노드의 위치를 저장하는 Head가 반드시 필요하고 Tail을 두면 맨 뒤 추가가 훨씬 빨라짐

## Singly Linked List

![image.png](/images/SW%EB%AC%B8%EC%A0%9C%ED%95%B4%EA%B2%B0%EA%B8%B0%EB%B3%B8%20-%20LinkedList/image.png)

한 방향으로만 이동

## java.util.LinkedList

```jsx
List<String> list = new LinkedList<>();
list.add("A");
list.add(0,"B");
list.get(1) // "A"
```
