---
title: "2. Java - 기본문법 & 제어문"
publishedAt: 2026-07-20
---
<!-- notion-import-source: notion-export-14d9e9508f374595b6e9691060b9d46e -->

## Hello Java

Java Spring Tool 기본설정

JVM, JRE, JDK

바이트코드

## 변수와 자료형

Primitive Type

→ 변수 자체에 값(리터럴)이 직접 저장됨

Local var / Instance var / Static var

Casting (Implicit / Explicit)

## 연산자

**산술 연산자**

- + - * / %

**비교 연산자**

- == ≠ > < ≥ ≤ instanceof

**논리 연산자**

- && || !

**단락평가**

→ 결과를 더이상 확인할 필요가 없는 경우 남은 조건 연산 안하고 넘어감

**삼항 연산자**

(조건문) ? (참) : (거짓)

## 제어문

## 조건문

- if
- if - else
- 중첩 if
- if - else if - else
- switch

## 반복문

- for
- while
- do - while

## 분기문

- break
- continue

[직업선호도검사(S형)결과_박진우.pdf](%EC%A7%81%EC%97%85%EC%84%A0%ED%98%B8%EB%8F%84%EA%B2%80%EC%82%AC(S%ED%98%95)%EA%B2%B0%EA%B3%BC_%EB%B0%95%EC%A7%84%EC%9A%B0.pdf)

```java
package com.ssafy.hw.step4;
import java.util.StringTokenizer;
import java.io.BufferedReader;
	import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class SpiderWeb {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st;
		
		int[] dx = {1,-1,0,0,1,1,-1,-1};
		int[] dy = {0,0,1,-1,1,-1,1,-1};
		
		int N = Integer.parseInt(br.readLine());
		int[][] map = new int[N][N];
		int[][] web = new int[N][N];
		
		//drawing map
		for (int i = 0 ; i < N ; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0 ; j < N ; j++) {
				map[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		st = new StringTokenizer(br.readLine());
		int startX = Integer.parseInt(st.nextToken());
		int startY = Integer.parseInt(st.nextToken());
		
		
		//search east
		if (map[startX][startY] == 0) web[startX][startY] = 1;
		for (int k = 0 ; k < 8 ; k++) {
			int warn = 0;
			for (int i = 0; startX + i * dx[k] < N && startX + i * dx[k] >= 0 && warn < 2 ; i++) {
				if (map[startX + i * dx[k]][startY + i * dy[k]] == 0) {
					web[startX + i * dx[k]][startY + i * dy[k]] = 1;
					warn = 0;
				} else warn++;
			}
		}
	
		for (int i = 0 ; i < N ; i++) {
			for (int j = 0 ; j < N ; j++) {
				bw.write(web[i][j] + " ");
			}
			System.out.println();
		}
	}
}

```
