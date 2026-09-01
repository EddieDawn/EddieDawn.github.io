---
title: "SW문제해결기본 - String"
publishedAt: 2026-09-01
---
<!-- notion-import-source: notion-page-3ce154b95f67809a855cddf061e674d5 -->

## 문자 표현

## ASCII (American Standard Code for Infotmation Interchange)

48 : 0
65: A
97: a

→ 이 정도는 외우면 좋을 수도 있을지도?

## Unicode

ASCII의 단일 체계 한계를 보완해서 나옴
U+XXXX (16진수) 형태로 표기

## 유니코드 인코딩 (UTF)

뭐 그런게 있다. 지금은 UTF-8을 제일 많이 쓴다는 것만 알고 있자.

## char

문자 하나를 담는 기본 자료형. 크기는 2byte
작은따옴표로만 감싸서 써야함 (큰따옴표는  String임)
문자와 숫자를 자유롭게 오갈 수 있음.

```java
public class String01_문자표현 {
	public static void main(String[] args) {
		char ch = 'A';
		System.out.println(ch);
		
		int i = ch;
		System.out.println(i);
		
		System.out.println(ch + 1); //implicit type casting
		
		System.out.println((char)(ch + 1)); //explicit type casting
		
		char ch2 = 'A' + 1;
		System.out.println(ch2);
		
		char char5 = '5';
		System.out.println((int)char5);
		
		int int5 = char5 - '0';
		System.out.println(int5);
	}
}
```

## 문자열 (String)

Chracater들의 나열. Reference type이다.

## 메모리 배치

java.lang.String 클래스 이런게 있어요

- hash값
- 문자열의 길이
- 문자열 데이터 시작점
- 실제 문자 배열에 대한 참조

![image.png](/images/SW%EB%AC%B8%EC%A0%9C%ED%95%B4%EA%B2%B0%EA%B8%B0%EB%B3%B8%20-%20String/image.png)

## String 클래스 특

- 불변: 한 번 생성된 String객테는 내부 내용 변경 불가능.
- Heap에 저장 + String Pool→ 동일 리터럴이면 이미 존재하는 객체 사용

## String 생성

- 리터럴(Literal) 사용
- 생성자 사용

![image.png](/images/SW%EB%AC%B8%EC%A0%9C%ED%95%B4%EA%B2%B0%EA%B8%B0%EB%B3%B8%20-%20String/image%201.png)

## String Method

- length()
- charAt(int index)
- contains(CharSequence s)
- equals(Object anObject)
- compareTo(String anotherString)
- indexOf(String str)

등등..

## String vs StringBuilder

```java
// 1. String: 반복마다 객체 만들기 (느림)
String s = "";
for (int i = 0 ; i < 100000 ; i++) s += "a";

// 2. StringBuilder: 하나의 객체를 계속 수정 (빠름)
StringBuilder sb = new StringBuilder();
for (int i = 0 ; i < 100000 ; i++) sb.append("a");
String result = sb.toString(); 
```

## Palindrome

→ 앞에서 읽는 것과 뒤에서부터 읽는 것이 동일한 문자열 ex) level, racecar, 기러기, 토마토

1. 반복문을 통해서 뒤에서 읽어오기
2. StringBuilder 또는 StringBuffer의 resverse() 활용
3. 양 끝에서 시작해서  swap을 통해 뒤집기

```java
public class String05_회문 {
	public static void main(String[] args) {
		String[] words = { "level", "racecar", "기러기", "토마토", "hello" };
		
		for(String word : words) {
			System.out.println(reverseFor((word)));
		}
		
		System.out.println("///////////////////////////////////////////////////");
		
		for(String word : words) {
			System.out.println(reverseStringBuilder((word)));
		}
		
		System.out.println("///////////////////////////////////////////////////");
		
		for(String word : words) {
			System.out.println(reverseSwap((word)));
		}

	}
	
	// 1. 뒤에서 읽기
	public static String reverseFor(String str) {
		
		String tmp = "";
		for (int i = str.length() - 1 ; i >= 0 ; i--) {
			tmp += str.charAt(i);
		}
		
		return tmp;
	}
	
	// 2. reverse() 사용
	public static String reverseStringBuilder(String str) {
//		StringBuilder sb = new StringBuilder();
//		sb.append(str);
//		sb.reverse();
//		
//		return sb.toString();
		
		return new StringBuilder(str).reverse().toString();
	}
	
	// 3. swap 방식
	public static String reverseSwap(String str) {
		char[] chars = str.toCharArray();
		
		for (int i = 0, j = str.length()-1 ; i < j ; i++, j--) {
			char tmp = chars[i];
			chars[i] = chars[j];
			chars[j] = tmp;
		}
		return new String(chars);
	}
}
```

## 근데 사실 진짜 안뒤집고  Palindrome인지 판별만 해도 됨

![image.png](/images/SW%EB%AC%B8%EC%A0%9C%ED%95%B4%EA%B2%B0%EA%B8%B0%EB%B3%B8%20-%20String/image%202.png)

## ASCII to Integer, Integer to ASCII

```java
public static int atoi (String strNumber) {
 int value = 0;
 for (int i = 0 ; i < strNumber.length() - 1; i++) {
	 value = (value * 10) + strNumber.charAt(i) - '0';
 }
 return value
}
 
 ////////////////////////////////////////////////////////////
 
public static String itoa (int num) {
	StringBuilder sb = new StringBuilder()
	do {
		sb.append((char)(number % 10 + '0'));
		number /= 10;
	} while (num > 0)
	return sb.reverse.toString();
}

//////////////////////////////////////////////////////////////
사실 이것밖에 안쓸걸?

Integer.parseInt(strNumber);

String.valueOf(num);
근데 이게 더편함ㅋㅋ
num + "";
```

## 패턴 매칭

## Brute Force

![image.png](/images/SW%EB%AC%B8%EC%A0%9C%ED%95%B4%EA%B2%B0%EA%B8%B0%EB%B3%B8%20-%20String/image%203.png)

![image.png](/images/SW%EB%AC%B8%EC%A0%9C%ED%95%B4%EA%B2%B0%EA%B8%B0%EB%B3%B8%20-%20String/image%204.png)

```java
	 public class String07_브루트포스 {
	public static void main(String[] args) {
		String text = "This iss a book";
		String pattern = "iss";

		
		System.out.println(bruteForce(text, pattern));
	}

	
	public static int bruteForce(String t, String p) {
		
		for (int i = 0 ; i < t.length() - p.length() + 1 ; i++) {
			int cnt = 0;
			for (int j = 0 ; j < p.length() ; j++) {
				if(t.charAt(i + j) == p.charAt(j)) cnt++;
			}
			if (cnt == p.length()) return i;
		}
		return -1;
	}
}

```
