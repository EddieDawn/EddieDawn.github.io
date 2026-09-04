---
title: "SW문제해결기본 - Sort"
publishedAt: 2026-09-04
---
<!-- notion-import-source: notion-page-3d1154b95f6780c6abe7e7800a0fa434 -->

## Sort

두 개 이상의 자료를 특정 기준(오름차순 or 내림차순)에 따라 다시 나열하는 것

비교 기반 정렬 vs 비교하지 않는 정렬

## Selection Sort

정렬되지 않은 구간에서 가장 작은(or 큰) 원소를 찾아 그 구간의 맨 앞(또는 뒤)로 보내는 과정을 반복
O(n^2)
같은 값의 순서가 바뀔 수 있다 → 불안정 정렬

1. 정렬되지 않은 구간에서 최솟값을 찾는다.
2. 그 값을 구간의 맨 앞 원소와 교환(swap)한다.
3. 맨 앞 원소를 제외한 나머지 구간에 같은 과정을 반복한다.

```java
import java.util.Arrays;

/**
 * [선택 정렬(Selection Sort)]
 *
 * 정렬되지 않은 구간에서 가장 작은 값을 골라 그 구간의 맨 앞과 교환한다. i번째 반복이 끝나면 0번부터 i번까지의 값이 최종 위치에
 * 확정된다.
 *
 * 특징 - 입력 상태와 관계없이 비교 횟수가 거의 같다: O(N^2) - 한 회전에 교환은 최대 한 번: 전체 교환 횟수는 N-1번 이하 -
 * 배열 내부에서 정렬하므로 추가 공간은 O(1) - 멀리 떨어진 두 원소를 교환하므로 불안정 정렬
 */
public class Sort01_SelectionSort {
	public static void main(String[] args) {
		int[] numbers = { 64, 25, 10, 22, 11 };

		selectionSort(numbers);

		System.out.println(Arrays.toString(numbers));
	}

	static void selectionSort(int[] numbers) {
		for (int i = 0; i < numbers.length - 1; i++) {
			int minIdx = i;

			for (int j = i + 1; j < numbers.length - 1; j++) {
				if (numbers[j] < numbers[minIdx])
					minIdx = j;
			}
			int tmp = numbers[i];
			numbers[i] = numbers[minIdx];
			numbers[minIdx] = tmp;
		}
	}
}

```

## 

## Insertion Sort

앞쪽의 정렬된 부분에 새 원소를 끼워 넣는 방식
O(n^2)
안정 정렬

정렬도지 않은 부분집합 U의 원소를 하나씩 꺼내어 S의 마지막 원소부터 비교하며 위치 찾아 삽입

```java
	import java.util.Arrays;

/**
 * [삽입 정렬(Insertion Sort)]
 *
 * 카드 패를 정리하듯, 현재 값을 왼쪽의 이미 정렬된 구간에 끼워 넣는다. 현재 값을 key에 보관하고, key보다 큰 값들을 한 칸씩
 * 오른쪽으로 민 뒤 비어 있는 위치에 key를 넣는 것이 핵심이다.
 *
 * 특징 - 이미 정렬된 배열: O(N) - 역순 배열: O(N^2) - 추가 공간: O(1) - 같은 값은 밀지 않으므로 원래 순서가
 * 유지되는 안정 정렬
 */
public class Sort02_InsertionSort {
	static int[] numbers;

	public static void main(String[] args) {
		numbers = new int[] { 69, 10, 30, 2, 16, 8, 31, 22 };

		insertionSort();
		System.out.println(Arrays.toString(numbers));
	}

	static void insertionSort() {
		for (int i = 1; i < numbers.length; i++) {
			int key = numbers[i];
			int pos = i - 1;

			while (pos >= 0 && numbers[pos] > key) {
				numbers[pos + 1] = numbers[pos];
				pos--;
			}

			numbers[pos + 1] = key;

		}
	}
}

```

![image.png](/images/SW%EB%AC%B8%EC%A0%9C%ED%95%B4%EA%B2%B0%EA%B8%B0%EB%B3%B8%20-%20Sort/image.png)

## Counting Sort

값을 서로 비교하지 않고, 각 값이 몇 개씩 있는지 세어서 정렬하는 알고리즘
값 자체를 배열의 인덱스로 사용 → 정수(또는 정수로 바꿀 수 있는 자료)만 정렬 가능
배열의 크기를 정하려면 데이터 중 가장 큰 값을 미리 알아야 한다

![image.png](/images/SW%EB%AC%B8%EC%A0%9C%ED%95%B4%EA%B2%B0%EA%B8%B0%EB%B3%B8%20-%20Sort/image%201.png)

![image.png](/images/SW%EB%AC%B8%EC%A0%9C%ED%95%B4%EA%B2%B0%EA%B8%B0%EB%B3%B8%20-%20Sort/image%202.png)

과정은 그림을 보고 이해해야할거임

```java
import java.util.Arrays;

/**
 * [카운팅 정렬(Counting Sort)]
 *
 * 값을 직접 비교하지 않고 각 값이 몇 번 나타나는지를 센다. 누적합은 각 값이 정렬 결과에서 차지하는 구간의 끝 위치를 알려 준다. 원본을
 * 뒤에서부터 읽어 결과 배열에 놓으면 같은 값의 원래 순서가 유지된다.
 *
 * 시간 복잡도: O(N + K), 추가 공간: O(N + K) K는 최댓값 자체가 아니라 '최댓값 - 최솟값 + 1'인 값의 범위다.
 *
 */
public class Sort03_CountingSort {
	public static void main(String[] args) {
		int[] numbers = { 0, 4, 1, 3, 1, 2, 4, 1 };

		System.out.println(Arrays.toString(countingSort(numbers)));
	}

	static int[] countingSort(int[] numbers) {
		int N = numbers.length;
		int[] sortedArr = new int[N];

		// 1. 가장 큰 값을 찾는다.
		int maxValue = -1;
		for (int i = 0; i < N; i++) {
			if (numbers[i] > maxValue)
				maxValue = numbers[i];
		}

		// 2. Counting
		int[] count = new int[maxValue + 1];
		for (int i = 0; i < N; i++) {
			count[numbers[i]]++;
		}

		// 3. cumulative sum
		for (int i = 1; i < count.length; i++) {
			count[i] += count[i - 1];
		}

		// 4. reverse traversal
		for (int i = N - 1; i >= 0; i--) {
//			int willBeSorted = numbers[i];
//			int index = --count[willBeSorted];
//			sortedArr[index] = numbers[i];

			sortedArr[--count[numbers[i]]] = numbers[i];
		}

		return sortedArr;
	}
}

```

## Radix Sort

원소끼리 크기를 비교하는 대신 자릿수를 기준으로 여러 번 분류해서 정렬하는 알고리즘
1의 자리 → 10의 자리 → 100의 자리 순으로 정렬
각 자리 정렬할 때는 반드시 안정 정렬을 사용해야 함

```java
import java.util.Arrays;

/**
 * [LSD 기수 정렬(Radix Sort)]
 *
 * 1의 자리, 10의 자리, 100의 자리처럼 낮은 자릿수부터 차례로 정렬한다. 앞 단계에서 맞춘 순서를 보존해야 전체 값이 올바르게
 * 정렬되므로, 각 자릿수는 반드시 안정 정렬로 처리해야 한다. 이 예제는 카운팅 정렬을 사용한다.
 *
 * 시간 복잡도: O(D * (N + 10)), 추가 공간: O(N + 10) D는 가장 큰 값의 자릿수다. 이 기본 구현은 교안 범위와 같이
 * 0 이상의 정수만 지원한다.
 */
public class Sort04_RadixSort {
	public static void main(String[] args) {
		int[] numbers = { 170, 45, 75, 90, 802, 24, 2, 66 };
		radixSort(numbers);
		System.out.println(Arrays.toString(numbers));
	}

	static void radixSort(int[] numbers) {
		// 1. find max value
		int max = numbers[0];
		for (int number : numbers) {
			max = Math.max(number, max);
		}

		// 2. sort by digits
		for (int exp = 1; max / exp > 0; exp *= 10) {
			countsortByDigit(numbers, exp);
		}
	}

	static void countsortByDigit(int[] numbers, int exp) {
		int N = numbers.length;
		int[] sortedArr = new int[N];
		int[] count = new int[10];

		for (int i = 0; i < N; i++) {
			int idx = (numbers[i] / exp) % 10;
			count[idx]++;
		}

		for (int i = 1; i < count.length; i++) {
			count[i] += count[i - 1];
		}

		for (int i = N - 1; i >= 0; i--) {
			int idx = (numbers[i] / exp) % 10;
			sortedArr[--count[idx]] = numbers[i];
		}

		for (int i = 0; i < N; i++) {
			numbers[i] = sortedArr[i];
		}
	}
}

```
