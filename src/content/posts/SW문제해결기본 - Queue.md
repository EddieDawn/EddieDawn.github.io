---
title: "SW문제해결기본 - Queue"
publishedAt: 2026-09-02
---
<!-- notion-import-source: notion-page-3cf154b95f6780579d8fddf9aaf4d8ac -->

## Queue란?

먼저 들어온 자료가 먼저 나가는 선형 FIFO(선입선출) 구조의 자료구조

## Queue의 주요 연산

- createQueue
- enQueue
- deQueue
- peel
- isEmpty
- isFull

## Queue의 종류

- Linear Queue
- Circular Queue
- Linked Queue
- Priority Queue
- Deque

## Queue의 활용

## java.util.Queue

인터페이스므로 실제 객체는 ArrayDeque 또는 LinkedList로 구현한다

```jsx
// 1. ArrayDeque로 선언하기
Queue<Integer> q = new ArrayDeque<>();

// 2. LinkedList로 구현하기
Queue<Integer> q = new LinkedList<>();
```

## Deque

양쪽 끝에서 삽입과 삭제가 모두 가능한 자료구조

### 주요 연산

![image.png](/images/SW%EB%AC%B8%EC%A0%9C%ED%95%B4%EA%B2%B0%EA%B8%B0%EB%B3%B8%20-%20Queue/image.png)

```jsx
Deque<String> dq = new ArrayDeque<>();
```

## Buffer

데이터를 한 곳에서 다른 곳으로 옮기는 동안 잠시 담아 두는 메모리 영역

## ❗️코테용으로 외웁시다❗️

## Stack

```jsx
Deque<Integer> stack = new ArrayDeque<>();

stack.push(1);
stack.pop();
stack.peek();
stack.isEmpty();
stack.size();
```

## Queue

```jsx
Queue<Integer> q = new ArrayDeque<>();

q.offer(1);
q.poll();
q.peek();
q.isEmpty();
q.size();
```

## Deque

```jsx
Deque<Integer> dq = new ArrayDeque<>();

dq.offerFirst(1);
dq.offerLast(2);
dq.pollFirst();
dq.pollLast();
dq.peekFirst();
dq.peekLast();
dq.isEmpty();
dq.size();
```
