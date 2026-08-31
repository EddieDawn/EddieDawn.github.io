---
title: "SW문제해결기본 - Array"
publishedAt: 2026-08-31
---
<!-- notion-import-source: notion-page-3cd154b95f6780b8938eefc335758f95 -->

## Array

동일한 데이터 타입의 값(0개 이상)들을 저장하기 위한 자료구조

![image.png](/images/SW%EB%AC%B8%EC%A0%9C%ED%95%B4%EA%B2%B0%EA%B8%B0%EB%B3%B8%20-%20Array/image.png)

## 필요 요소 3가지

1. 자료형
→ 배열을 이루는 자료형 (Primitive type, Reference type 전부 가능)
2. 배열 이름
→ 프로그램에서 사용할 배열의 이름 (주소 값 저장)
3. 길이
→ 배열을 이루는 요소의 값 (고정된 길이)

## 선언 방법

```java
자료형[] 배열이름 = new 자료형[배열길이]

//예시
int[] nums = new int[6]
```

## 자주 나오는 실수

- 배열의 길이는 arr.length , 문자열의 길이는 str.length()
- new int[n]의 기본값은 0
- b = a 는 얕은복사
- 배열 길이는 생성 후 변경이 불가함

## java.util.Arrays

반복문으로 직접 구현하기 전에 API가 있는지 먼저 생각해보자

## 2차원 배열

```java
// 2행 4열 배열 선언하기
int[][] arr = new int[2][4]
```

![image.png](/images/SW%EB%AC%B8%EC%A0%9C%ED%95%B4%EA%B2%B0%EA%B8%B0%EB%B3%B8%20-%20Array/image%201.png)

```java
int[][] scores = {{80, 80, 85, 100}, {100, 80, 75, 60}, {50, 90, 100, 100}}
```

![image.png](/images/SW%EB%AC%B8%EC%A0%9C%ED%95%B4%EA%B2%B0%EA%B8%B0%EB%B3%B8%20-%20Array/image%202.png)

<aside>
💡

달팽이순회 풀어보기

</aside>

## 가변길이 순회

![image.png](/images/SW%EB%AC%B8%EC%A0%9C%ED%95%B4%EA%B2%B0%EA%B8%B0%EB%B3%B8%20-%20Array/image%203.png)

![image.png](/images/SW%EB%AC%B8%EC%A0%9C%ED%95%B4%EA%B2%B0%EA%B8%B0%EB%B3%B8%20-%20Array/image%204.png)

생각해보기

## 배열의 응용

## 검색 (Search)

### 순차 검색 - 정렬 X

```java
//a : 1차원 배열, n : 배열 크기, key : 찾고있는 값
sequentialSearch(int[] a, int n, int key)
	i <- 0
	while(i < n and a[i] != key)
		i <- i+1;
	if(i < n) return i;
	else return -1;
```

시간 복잡도: O(n)

### 순차 검색 - 정렬 O

```java
//a : 1차원 배열, n : 배열 크기, key : 찾고있는 값
sequentialSearch(int[] a, int n, int key)
	for i in range from 0 to n-1:
		if a[i] == key: return i;
		else if a[i] > key: break;
	return -1;
```

시간 복잡도: O(n)

→ 정렬이 되어있던 안되어있던 순차검색은 O(n)임

## 카운팅 배열: 값을 인덱스로 쓰기

“몇 번 나왔는가”를 배열에 기록

```java
int[] cnt = new int[101];
for (int score: scores) cnt[score]++;
```

## 누적합(Prefix Sum): 구간합을 O(1)로

```java
int[] a = {3, 1, 4, 1, 5}
int[] sum = new int[a.length + 1];

for (int i = 0 ; i < a.length ; i++) {
	sum[i + 1] = sum[i] + a[i];
}
// sum = {0, 3, 4, 8 ,9, 14}

// 구간 [1, 3] 누적합 구하기
int l = 1, r = 3;
System.out.println(sum[r + 1] - sum[l])
```

## 델타를 이용한 이동

```java
//동서남북
int[] dx = {-1, 1, 0, 0}
int[] dy = {0, 0, 1, -1}

//우상 우하 좌하 좌상
int[] dx = {1, 1, -1, -1}
int[] dy = {1, -1, -1, 1}
```

활용 의사코드

```java
array[0 ... n01][0 ... n-1]
dr <- {-1, 1, 0, 0}
dc <- {0, 0, -1, 1}

for r in from 0 to n-1
	for c in from 0 to n-1
		for d from 0 to 3
			nr <- r + dr[d];
			nc <- c + dc[d];
			// 조건
			array[nr][nc] //필요한 연산 수행
```

하지만 IndexOutofBound가 뜨지 않으려면 가드레일이 필요함

```java
// 가드레일 (static을 써야 인스턴스 안만들고 편하게 꺼내쓸수있다.)
static boolean isIn(int r, int c) {
	return 0 <= r && r < N && 0 <= c && c < M;
}

for (...) {
	if (isIn(nr, nc)) sum += map[nr][nc];
}
```

## 전치행렬 (Transposed Martix)

행 → 열

열 → 행

## 배열 회전

### 90도 회전

![image.png](/images/SW%EB%AC%B8%EC%A0%9C%ED%95%B4%EA%B2%B0%EA%B8%B0%EB%B3%B8%20-%20Array/image%205.png)

### 180도 회전

![image.png](/images/SW%EB%AC%B8%EC%A0%9C%ED%95%B4%EA%B2%B0%EA%B8%B0%EB%B3%B8%20-%20Array/image%206.png)

```java
for (int i = 0 ; i < n ; i++) {
	for (int j = 0 ; j < n ; j++) {
		newArr[n-i-1][n-j-1] = arr[i][j]
	}
}
```

### 270도 회전

![image.png](/images/SW%EB%AC%B8%EC%A0%9C%ED%95%B4%EA%B2%B0%EA%B8%B0%EB%B3%B8%20-%20Array/image%207.png)

```java
for (int i = 0 ; i < n ; i++) {
	for (int j = 0 ; j < n ; j++) {
		newArr[n-1-j][i] = arr[i][j]
	}
}
```

그냥 90도 회전 함수 하나 만들어서 반복해서 꺼내 써도 됨.
