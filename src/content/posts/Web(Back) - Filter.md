---
title: "Web(Back) - Filter"
publishedAt: 2026-10-14
---
<!-- notion-import-source: notion-page-3f9154b95f6780b4ab79f76d96250f01 -->

## Listener

웹 애플리케이션의 이벤트를 감지하는 객체
서블릿 컨테이너가 특정 이벤트가 발생하면 자동으로 실행하는 처리용 객체

## 주요 Listener 인터페이스

![image.png](/images/Web%28Back%29%20-%20Filter/image.png)

## Listener 등록 방법

1. Annotation 등록

```java
package com.ssafy.listener;

import jakarta.servlet.ServletContextEvent;
import jakarta.servlet.ServletContextListener;
import jakarta.servlet.annotation.WebListener;

//ServletContextListener
//웹 어플리케이션이 시작 / 종료될 때
//리스너를 등록하는 방법 - 1. Annotation
@WebListener
public class MyListener implements ServletContextListener {
	@Override
	public void contextInitialized(ServletContextEvent sce) {
		//서버가 켜질 때 딱 한 번 실행이 된다
		//공통 설정값을 읽거나 초기 데이터 준비 등을 수행한다.
		System.out.println("Web Application initialized.");
	}
	
	@Override
	public void contextDestroyed(ServletContextEvent sce) {
		//서버가 꺼질 때 딱 한 번 수행이 된다
		//열어 둔 파일 또는 자원을 닫고 회수하는 역할
		System.out.println("Web Application terminated.");
	}
}
```

1. web.xml에 등록 (클래스에는 어노테이션을 붙이지 않기)

```xml
<?xml version="1.0" encoding="UTF-8"?>
<web-app id="WebApp_ID" version="2.4" xmlns="http://java.sun.com/xml/ns/j2ee" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://java.sun.com/xml/ns/j2ee http://java.sun.com/xml/ns/j2ee/web-app_2_4.xsd">
	<display-name>05_Filter</display-name>
	<!-- Listener를 등록해 보자 -->
	<listener>
		<listener-class>com.ssafy.listener.MyListener2</listener-class>
	</listener>
</web-app>

```

두 등록 방식 비교하기

- @WebListener: 코드만으로 간단히 등록, 간편하지만 실행 순서를 보장할 수는 없음
- web.xml <listener>: 초기화는 선언 순서, 종료는 역순으로 실행

## Filter

클라이언트의 요청과 서버 자원(Servlet/JSP) 사이에서 요청과 응답을 가로채 전·후 처리하는 객체
ex) 서블릿 인코딩 설정(UTF-8), 봇 차단, 게시물 비속어 검열
여러개 있을 수 있음 (필터 체인)

## Filter 구성요소

chain.doFilter()를 기준으로 나뉜다.

```java
package com.ssafy.filter;

import java.io.IOException;

import jakarta.servlet.Filter;
import jakarta.servlet.FilterChain;
import jakarta.servlet.ServletException;
import jakarta.servlet.ServletRequest;
import jakarta.servlet.ServletResponse;
import jakarta.servlet.annotation.WebFilter;

public class MyFilter implements Filter {
	
	@Override
	public void doFilter(ServletRequest req, ServletResponse resp, FilterChain chain)
			throws IOException, ServletException {

		
		//사전 처리 (요청이 들어갈 때)
		req.setCharacterEncoding("UTF-8");
		resp.setCharacterEncoding("UTF-8");
		
		/// 다음 순서(필터, 서블릿, JSP)로 넘기기 (구현 필수)
		chain.doFilter(req, resp);
		
		//사후 처리 
		System.out.println("Filter Responded");
	}
****
}
```

## Filter 활용

- 인코딩 처리
- 인증 / 인가 확인
- 로깅
- 보안 확인
- 압축 / 캐시 제어
- 등등

## Filter 등록

1. Annotation

```java
package com.ssafy.filter;

import java.io.IOException;

import jakarta.servlet.Filter;
import jakarta.servlet.FilterChain;
import jakarta.servlet.ServletException;
import jakarta.servlet.ServletRequest;
import jakarta.servlet.ServletResponse;
import jakarta.servlet.annotation.WebFilter;

@WebFilter("/*") // 1. Annotation 등록
public class MyFilter implements Filter {
	
	@Override
	public void doFilter(ServletRequest req, ServletResponse resp, FilterChain chain)
			throws IOException, ServletException {

		
		//사전 처리 (요청이 들어갈 때)
		req.setCharacterEncoding("UTF-8");
		resp.setCharacterEncoding("UTF-8");
		
		////////////////////////////////////
		/// 다음 순서(필터, 서블릿, JSP)로 넘기기 (구현 필수)
		chain.doFilter(req, resp);
		////////////////////////////////////
		
		//사후 처리 
		System.out.println("Filter Responded");
	}

}

```

![image.png](/images/Web%28Back%29%20-%20Filter/image%201.png)

1. web.xml

```java
<?xml version="1.0" encoding="UTF-8"?>
<web-app id="WebApp_ID" version="2.4" xmlns="http://java.sun.com/xml/ns/j2ee" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://java.sun.com/xml/ns/j2ee http://java.sun.com/xml/ns/j2ee/web-app_2_4.xsd">
	<display-name>05_Filter</display-name>
	
	<!-- 필터 등록 -->
	<filter>
		<filter-name>MyFilter2</filter-name>
		<filter-class>com.ssafy.filter.MyFilter2</filter-class>
	</filter>
	<filter-mapping>
		<filter-name>MyFilter2</filter-name>
		<url-pattern>"/*"</url-pattern>
	</filter-mapping>
</web-app>

```

<filter-mapping>의 선언 순서가 곧 전체 체인의 순서이다.

## Exception

프로그램 실행 중 발생하는 비정상적인 상황
(여기서는 web.xml방식만 알아보자)

```java
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>404 Page</title>
</head>
<body>
	<h2>간지나고 센스있게 만들어야 사용자들 화가 누그러짐 ㅋㅋ</h2>
	<%=request.getContextPath() + "요청 맞음?" %>
</body>
</html>
```

```xml
<?xml version="1.0" encoding="UTF-8"?>
<web-app id="WebApp_ID" version="2.4" xmlns="http://java.sun.com/xml/ns/j2ee" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://java.sun.com/xml/ns/j2ee http://java.sun.com/xml/ns/j2ee/web-app_2_4.xsd">
	<display-name>05_Filter</display-name>

	<error-page>
		<error-code>404</error-code>
		<location>/error/404.jsp</location>
	</error-page>
	<error-page>
		<error-code>500</error-code>
		<location>/error/500.jsp</location>
	</error-page>
	
	<!-- 코드 대신 예외클래스로 매핑도 가능함 -->
	<error-page>
		<exception-type>java.lang.RunTimeException</exception-type>
		<location>/error/500</location>
	</error-page>
</web-app>

```
