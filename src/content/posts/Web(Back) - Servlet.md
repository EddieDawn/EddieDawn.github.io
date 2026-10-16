---
title: "Web(Back) - Servlet"
publishedAt: 2026-10-06
---
<!-- notion-import-source: notion-page-3f1154b95f678040a436e072f29ef956 -->

## Web Architecture

![image.png](/images/Web%28Back%29%20-%20Servlet/image.png)

## Servlet

Server + Applet
요청 / 응답을 처리하는 Java 웹 컴포넌트

## Servlet 컨테이너가 대신 해 주는 일

- 요청 메시지를 분석해 request 객체로 만들어 준다. → 파라미터를 바로 꺼내 쓸 수 있음
- 응답 메시지의 형식을 갖춰 response 객체로 만들어 준다. → 그대로 출력만 하면 됨

## Servlet API

![image.png](/images/Web%28Back%29%20-%20Servlet/image%201.png)

## Servlet 등록방법

1. web.xml
2. Annotation

## Servlet 생명 주기 (Life Cycle)

![image.png](/images/Web%28Back%29%20-%20Servlet/image%202.png)

1. Servlet 클래스 로드
2. Servlet 인스턴스 생성
3. Servlet 인스턴스 초기화
4. 요청마다 웹 컨테이너가 service()를 호출함
5. 서비스 제거 전 destroy() 호출

## 자원

## URI (Uniform Resource Identifier)

자원을 식별하는 모든 방법

## URL (Uniform Resource Locator)

그 자원이 어디에 있고 어떻게 접근함?

## URN (Uniform Resource Name)

어딨는지는 모르겠고, 이 자원의 고유한 이름은 이거임

## URL 구성요소

![image.png](/images/Web%28Back%29%20-%20Servlet/image%203.png)
