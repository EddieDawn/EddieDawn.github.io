---
title: "Web (Back) - Cookie & Session"
publishedAt: 2026-10-12
---
<!-- notion-import-source: notion-page-3f7154b95f678081829ae39d4b774b41 -->

## HTTP (Hypertext Tansfer Protocol)

클라이언트와 서버가 요청·응답 메시지를 주고받는 애플리케이션 계층 프로토콜
http URI의 기본 포트: 80
https URI의 기본 포트: 443 이며, TLS로 통신 보호

## HTTP Request 메시지 구조

1. 시작 라인
메서드 + 경로 + 버전
ex) GET/01_AddCookie.jsp HTTP/1.1
2. 헤더
요청에 대한 부가 정보
Host, user-Agent, Cookie
3. 본문
서버로 보낼 데이터 (GET은 필요 X)

## HTTP Response 메시지 구조

1. 상태 라인
버전 + 상태 코드
    
    ex) HTTP/1.1 200 OK
    
2. 헤더
Content-Type, Set-Cookie
3. 본문
브라우저가 실제로 그려낼 HTML / 이미지 / JSON

## HTTP 주요 메서드

![image.png](/images/Web%20%28Back%29%20-%20Cookie%20%26%20Session/image.png)

## HTTP 특징 - Stateless

1. 클라이언트 상태를 자동으로 저장하지 않음
2. 각 요청을 처리하는 데 필요한 상태 장보를 요청에 포함해야 함
3. 서버 확장 / 부하 분산에 유리
4. 쿠키 / 서버 세션 등으로 애플리케이션 상태를 유지

## 상태 유지 방식

1. Cookie
손님이 신분증 들고 다니기
2. Session
가게가 손님별 보관함을 두고 번호표만 주기

## HTTP 상태 코드

![image.png](/images/Web%20%28Back%29%20-%20Cookie%20%26%20Session/image%201.png)

![image.png](/images/Web%20%28Back%29%20-%20Cookie%20%26%20Session/image%202.png)

## Cookie

서버가 Set-Cookie 응답 헤더로 보내 브라우저가 저장하는 작은 데이터 조각
서버가 손님에게 쥐어주는 “쪽지”

ex) 오늘 하루 이 창 보지 않기 / 최근 본 상품 / 로그인 없는 장바구니

! 사용자나 스크립트가 접근 가능함. 보호 필요 !

## Cookie 사용 목적

- 세션 관리 (세션 식별자, 장바구니 등)에 사용
- 사용자가 설정한 환경을 기억해 맞춤 화면 제공
- (사용자 동의와 정책에 따라) 이용 패턴 분석 & 맞춤 광고에 활용

## Cookie 동작 순서

1. Client가 요청 생성
2. 서버가 Cookie 생성, 응답의 Set-Cookie 헤더로 전달
3. 브라우저가 Cookie 저장, 조건이 맞는 요청의 Cookie 헤더로 전송

![image.png](/images/Web%20%28Back%29%20-%20Cookie%20%26%20Session/image%203.png)

## Cookie 특징

- 이름, 값, 만료 시점, 도메인, 경로, Secure, HttpOnly 등 속성으로 구성
- setMaxAge(int seconds) : 쿠키 수명 정하기

![image.png](/images/Web%20%28Back%29%20-%20Cookie%20%26%20Session/image%204.png)

## JSP 기본 객체 영역

![image.png](/images/Web%20%28Back%29%20-%20Cookie%20%26%20Session/image%205.png)

![image.png](/images/Web%20%28Back%29%20-%20Cookie%20%26%20Session/image%206.png)

![image.png](/images/Web%20%28Back%29%20-%20Cookie%20%26%20Session/image%207.png)

## Session

여러 요청에서 같은 클라이언트를 식별하고 정보를 유지하는 서버 측 기능 (Server side)
컨테이너가 할당한 session ID로 세션을 식별

## Session 특징

- 세션 = 서버가 손님마다 만들어 두는 “보관함”
- 손님에게는 보관함 번호표(Session ID)만 쿠키로 줌
- 실제 데이터는 서버 측 저장소에만 있음
- 데이터는 서버 측에 있지만 session id가 탈취되면 세션 하이재킹 위험이 있음.
- 세션 속성은 서버 자원을 사용하므로 크기와 수명을 관리해야 한다

## Session 동작 순서

![image.png](/images/Web%20%28Back%29%20-%20Cookie%20%26%20Session/image%208.png)

![image.png](/images/Web%20%28Back%29%20-%20Cookie%20%26%20Session/image%209.png)

## 로그아웃 시 뭘 지워야할까?

![image.png](/images/Web%20%28Back%29%20-%20Cookie%20%26%20Session/image%2010.png)

![image.png](/images/Web%20%28Back%29%20-%20Cookie%20%26%20Session/image%2011.png)

,
