---
title: "SW문제해결응용 - 부분집합"
publishedAt: 2026-09-08
---
<!-- notion-import-source: notion-page-3d4154b95f6780149e2ac0184297718d -->

## 컴퓨터 수 표현

## Binary

### 2진수 읽기

### 10진수 → 2진수

## Octal

## Hexadecimal

### 2진수, 8진수, 16진수의 관계

## 컴퓨터의 음수 표현

## 비트 연산자

&, |, ^, ~, <<, >>

## 부분집합

## 반복문

```java
import java.util.Arrays;

/**
 * [중첩 반복문으로 만드는 부분집합]
 *
 * 원소마다 '포함하지 않음(0)'과 '포함함(1)' 두 경우를 반복문으로 표현한다. 흐름이 눈에 보이므로 처음 개념을 익힐 때 좋지만,
 * 원소가 N개면 반복문도 N개가 필요하다. 이 예제는 그 한계를 분명히 보이기 위해 PDF와 같이 원소 4개 전용으로 작성한다.
 */
public class 부분집합01_반복문 {
	public static void main(String[] args) {
		String[] ingredients = { "단무지", "햄", "오이", "지단" };

		int[] sel = new int[ingredients.length];

		for (int a = 0; a < 2; a++) {
			sel[0] = a;
			for (int b = 0; b < 2; b++) {
				sel[1] = b;
				for (int c = 0; c < 2; c++) {
					sel[2] = c;
					for (int d = 0; d < 2; d++) {
						sel[3] = d;
						//////////////////////////
//						for (int i = 0; i < ingredients.length; i++) {
//							if (sel[i] == 1)
//								System.out.println(ingredients[i]);
//						}
						System.out.println(Arrays.toString(sel));
					}
				} // 세 번째 재료 고려
			} // 두 번째 재료 고려
		} // 첫 번째 재료 고려
	}
}

```

## 비트마스킹

```java
/**
 * [비트마스킹으로 만드는 부분집합]
 *
 * N비트 정수 하나가 부분집합 하나를 나타낸다. j번째 비트가 1이면 elements[j]를 포함하고, 0이면 포함하지 않는다. 0부터 (1
 * << N)-1까지 순회하면 공집합부터 전체 집합까지 정확히 2^N개가 나온다.
 *
 * 모든 부분집합을 실제 List로 저장하면 O(N * 2^N) 메모리가 필요하다. 이 학습용 메서드는 실수로 지나치게 큰 결과를 만들지
 * 않도록 N을 20 이하로 제한한다.
 */
public class 부분집합02_비트마스킹 {
	public static void main(String[] args) {
		String[] ingredients = { "단무지", "햄", "오이" };

		int N = ingredients.length;

		for (int i = 0; i < (1 << N); i++) {
			for (int j = 0; j < N; j++) {
				if ((i & (1 << j)) != 0) {
					System.out.println(ingredients[j]);
				}
			}
			System.out.println("김밥");
		} // 부분집합 i 반복문
	}
}

```

## 재귀함수

```java

```
