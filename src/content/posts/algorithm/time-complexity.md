---
title: "시간 복잡도를 보는 첫 기준"
description: "입력 크기가 커질 때 알고리즘의 실행 시간이 어떻게 달라지는지 정리한다."
publishedAt: 2026-08-13
category: "algorithm"
tags: ["algorithm", "complexity"]
---

# 시간 복잡도

시간 복잡도는 입력 크기 `n`이 커질 때 연산 횟수가 얼마나 늘어나는지를 나타낸다.

```java
for (int i = 0; i < n; i++) {
  System.out.println(i);
}
```

위 반복문은 `n`번 실행되므로 시간 복잡도는 `O(n)`이다.
