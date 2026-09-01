---
title: "SW문제해결기본 - Stack"
publishedAt: 2026-09-01
---
<!-- notion-import-source: notion-page-3ce154b95f6780ba843bd7acfcb3a428 -->

## Stack이란?

LIFO(후입선출) 선형 자료구조

## Stack의 주요 연산

- push
- pop
- empty
- peek
- size

! pop과 peek은 스택이 비어있는건 아닌지 먼저 확인하고 쓰자

## 배열로 stack 구현

```java
/**
 * 고정 길이 배열로 스택을 직접 구현하는 예제이다.
 *
 * top의 의미를 "마지막으로 저장된 원소의 인덱스"로 정한다. - 공백 스택: top == -1 - push: top을 먼저 1 증가시킨
 * 뒤 값을 저장 - pop: top 위치의 값을 꺼낸 뒤 top을 1 감소
 *
 * 장점: 구현이 단순하고 모든 기본 연산이 O(1)이다. 단점: 배열의 크기가 고정되어 있으므로 가득 차면 더 넣을 수 없다.
 */
class MyArrayStack {
	private int top = -1;
	private String stack[];

	public MyArrayStack(int num) {
		this.stack = new String[num];
	}

	void push(String element) {
		if (isFull()) {
			System.out.println("이미 스택이 가득 찼어요 ㅠㅠ");
			return;
		}

		stack[++top] = element;
	}

	String pop() {
		if (isEmpty()) {
			System.out.println("스택이 비어있어요 ㅠㅠ");
			return null;
		}
		return stack[top--];
	}

	String peek() {
		if (isEmpty()) {
			System.out.println("스택이 비어있어요 ㅠㅠ");
			return null;
		}
		return stack[top];
	}

	boolean isFull() {
		return top == stack.length - 1;
	}

	boolean isEmpty() {
		return top == -1;
	}

}

public class Stack01_Array구현 {
	public static void main(String[] args) {
		MyArrayStack stack = new MyArrayStack(100);

		stack.push("A");
		stack.push("B");
		stack.push("C");
		stack.push("D");

		System.out.println(stack.pop());
		System.out.println(stack.pop());
		System.out.println(stack.pop());
		System.out.println(stack.pop());

	}
}

```

## 이미 제네릭이 존재하긴 함

```java
import java.util.Stack;

/**
 * java.util.Stack의 주요 연산을 확인하는 예제이다.
 *
 * 스택은 마지막에 넣은 원소를 가장 먼저 꺼내는 LIFO(Last-In First-Out) 자료구조이다. push, pop, peek는 모두
 * 스택의 맨 위(top)에서 동작한다.
 *
 * 시간 복잡도: push, pop, peek, isEmpty, size는 일반적으로 O(1) 주의할 점: 비어 있는 스택에서 pop 또는
 * peek를 호출하면 예외가 발생한다.
 */
public class Stack02_API {
	public static void main(String[] args) {
		// 제네릭의 자료형에는 int가 아니라 래퍼 클래스인 Integer를 사용한다.
		Stack<Integer> stack = new Stack<>();

		// push(item): 스택의 맨 위에 원소를 추가한다.
		stack.push(1);
		stack.push(2);
		stack.push(3);
		// peek(): 맨 위 원소를 확인만 한다. 원소는 삭제되지 않는다.
		System.out.println(stack.peek());
		// pop(): 맨 위 원소를 꺼내 반환하며, 스택에서는 삭제한다.
		System.out.println(stack.pop());

		// size(): 현재 저장된 원소의 수
		System.out.println(stack.size());
		// isEmpty(): 스택이 비었는지 확인
		System.out.println(stack.isEmpty());

		for (; !stack.isEmpty();) {
			stack.pop();
		}

		System.out.println(stack.isEmpty());

		// 스택 싹다 비워버리기
		stack.push(1);
		stack.push(2);
		stack.push(3);

		stack.clear();
		System.out.println(stack.isEmpty());

		stack.push(1);
		stack.push(2);
		stack.push(3);

		stack = new Stack<Integer>();
		System.out.println(stack.isEmpty());
	}
}

```

## Stack 활용

## 괄호 짝 검사

![image.png](/images/SW%EB%AC%B8%EC%A0%9C%ED%95%B4%EA%B2%B0%EA%B8%B0%EB%B3%B8%20-%20Stack/image.png)

## Function Call

![image.png](/images/SW%EB%AC%B8%EC%A0%9C%ED%95%B4%EA%B2%B0%EA%B8%B0%EB%B3%B8%20-%20Stack/image%201.png)

## Recursive Function

![image.png](/images/SW%EB%AC%B8%EC%A0%9C%ED%95%B4%EA%B2%B0%EA%B8%B0%EB%B3%B8%20-%20Stack/image%202.png)

![image.png](/images/SW%EB%AC%B8%EC%A0%9C%ED%95%B4%EA%B2%B0%EA%B8%B0%EB%B3%B8%20-%20Stack/image%203.png)
