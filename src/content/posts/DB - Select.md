---
title: "DB - Select"
publishedAt: 2026-10-16
---
<!-- notion-import-source: notion-page-3fb154b95f678046b836cdd0e1f24d20 -->

## DataBase

## DB가 필요한 이유

- 중복·불일치 방지
- 동시성·무결성 보장
- 보안

## DB의 특징

- 통합성
- 독립성
- 무결성
- 보안성
- 일관성
- 공유성
- 회복성

## DBMS (DataBase Management System)

사용자와 DB사이에서 데이터베이스를 생성, 정의, 공유, 관리하는 기능의 프로그램

## 관계형 데이터베이스

데이터를 행과 열로 구성된 테이블 형태로 관리하는 데이터베이스

## Schema

데이터베이스에서 자료의 구조, 표현방법, 관계 등 전반적인 명세를 기술한 것

![image.png](/images/DB%20-%20Select/image.png)

## 기본 키(Primary Key)와 외래 키(Foreign Key)

- PK
행을 유일하게 구분하는 열 또는 열의 조합
- FK
다른 테이블의 기본키나 UNIQUE키를 참조하는 열

## SQL (Structured Query Language)

관계형 데이터베이스에서 데이터 조작과 데이터 정의를 위해 사용하는 언어

- 데이터 조회
- 데이터 삽입·삭제·수정
- 데이터베이스 객체 생성·변경·삭제
- DB사용자 생성·삭제·권한 제어

## SQL 특징

- 비교적 간결한 문법으로 데이터를 다룬다
- SQL 키워드는 대소문자를 구분하지 않는 것이 일반적이다. (하지만 대문자 권장)

## SQL의 분류

- DDL (Data Definition Language)
데이터베이스 객체 구조 정의/수정/삭제
- DML (Data Manipulation Language)
데이터베이스 조작 (CRUD)
- DCL (Data Control Language)
사용자 권한 및 보안 제어
- TCL (Transaction Control Language)
DML 수행 결과를 트랜잭션 단위로 제어

![image.png](/images/DB%20-%20Select/image%201.png)

## SELECT

## MySQL 주석

```sql
-- 한 줄 주석 --

# 한 줄 주석

/*
	여러 줄 주석
*/
```

## SELECT문

테이블에서 레코드를 조회하기 위해 사용됨

![image.png](/images/DB%20-%20Select/image%202.png)

## SELECT문 작성 순서 vs 실행 순서 (별칭이 WHERE에서 안 되는 이유)

![image.png](/images/DB%20-%20Select/image%203.png)

## WHERE

조건에 맞는 레코드를 조회하기 위해 사용
UPDATE, DELETE문에서도 사용 가능

## SQL의 논리 연산자

![image.png](/images/DB%20-%20Select/image%204.png)

## SQL의 비교 연산자

![image.png](/images/DB%20-%20Select/image%205.png)

## 실습 코드

```sql
USE SSAFY_CORPORATION;

-- 한 줄 주석
# 한 줄 주석
/*
	여러 줄 주석
*/
 
# Q1. 모든 사원 모든 정보 검색
SELECT *
FROM emp;

# Q2-1. 사원이 근무하는 부서 번호
SELECT DISTINCT deptno
FROM emp;

# Q2-2. 사원이 근무하는 부서 번호(중복제거)
SELECT DISTINCT deptno, job
FROM emp;

# Q3. 사원의 이름, 부서번호, 업무 조회
SELECT DISTINCT ename, deptno, job
FROM emp;

# Q4. 사원의 이름, 사번, 급여*12 (연봉), 업무 조회
SELECT DISTINCT ename "이 름", empno 사번, sal * 12 as 연봉, job "업무"
FROM emp;

# Q5. 사원의 이름, 사번, 커미션, 급여, 커미션 포함 급여 조회
SELECT DISTINCT ename, empno, comm, sal, sal+comm as "급여 + 커미션 NULL처리 X", sal + IFNULL(comm, 0)
FROM emp;

# Q6. 모든 사원의 사번, 이름, 급여, 급여 등급  조회 (5000 이상 -> 높은연봉, 2000 이상 -> 평균 연봉, 그 외 -> 낮은연봉)
SELECT empno, ename, sal,
	CASE
		WHEN sal >= 5000 THEN "고액급여"
		when sal >= 2000 THEN "평균급여"
		ELSE "낮은급여"
	END AS "급여등급"
FROM emp;

# Q7. 부서 번호가 30인 사원중 급여가 1500 이상인 사원의 이름, 급여, 부서번호 조회
SELECT ename, sal, deptno
FROM emp
WHERE deptno = 30 AND sal <= 1500;

# Q8. 부서번호가 20 또는 30인 부서에서 근무하는 사원의 사번, 이름, 부서번호 조회
SELECT empno, ename, deptno
FROM emp
-- WHERE deptno = 20 OR deptno = 30;
WHERE deptno IN (20, 30);

# Q9. 부서번호가 20,30이 아닌 부서에서 근무하는 사원의 사번, 이름, 부서번호 조회
SELECT empno, ename, deptno
FROM emp
-- WHERE deptno <> 20 AND deptno <> 30; --
WHERE NOT (deptno = 20 OR deptno = 30);

# Q10. 업무가 'MANAGER', 'ANALYST', 'PRESIDENT' 인 사원의 이름, 사번, 업무조회
SELECT empno, ename, deptno
FROM emp
WHERE job IN ('MANAGER', 'ANALYST', 'PRESIDENT');

# Q11. 부서번호가 10, 20이 아닌 사원의 사번, 이름, 부서번호 조회
SELECT empno, ename, deptno
FROM emp
WHERE deptno NOT IN (10, 20);

# Q12. 급여가 2000이상 3000이하 인 사원의 사번, 이름, 급여조회
SELECT empno, ename, deptno
FROM emp
-- WHERE sal >= 2000 AND sal <= 3000; --
WHERE sal BETWEEN 2000 AND 3000;

# Q13. 입사일이 1981년인 직원의 사번, 이름, 입사일 조회
SELECT empno, ename, hiredate
FROM emp
-- WHERE hiredate BETWEEN '1981-01-01' AND '1981-12-31'; --
WHERE YEAR(hiredate) = 1981;

# Q14. 커미션인 NULL 인 사원의 사번, 이름, 커미션 조회
SELECT empno, ename, hiredate
FROM emp
WHERE comm IS NULL;

# Q15. 커미션 NULL이 아닌 사원의 사번, 이름, 업무, 커미션 조회
SELECT empno, ename, hiredate
FROM emp
WHERE comm IS NOT NULL;

# Q16. 이름이 M으로 시작하는 사원의 사번, 이름 조회
SELECT empno, ename
FROM emp
WHERE ename LIKE 'M%';

# Q17. 이름에 E가 포함된 사원의 사번 이름 조회
SELECT empno, ename
FROM emp
WHERE ename LIKE '%M%';

# Q18. 이름의 세번째 알파벳이 'A'인 사원의 사번, 이름 조회
SELECT empno, ename
FROM emp
WHERE ename LIKE '__A%';

# Q19. 모든 직원의 모든 정보를 이름을 기준으로 내림차순 정렬
SELECT *
FROM emp
ORDER BY ename DESC;

# Q20. 모든 사원의 사번, 이름, 급여를 조회 (급여 내림차순)
SELECT *
FROM emp
ORDER BY sal DESC;

# Q21. 20, 30번 부서에 근무하는 사원의 사번, 이름, 부서번호, 급여 조회 (부서별 오름차순, 급여순 내림차순)
SELECT empno, ename, deptno, sal
FROM emp
WHERE deptno IN (20, 30)
ORDER BY deptno ASC, sal DESC;

# 급여 1 ~ 3위 출력
SELECT ename, sal
FROM emp
ORDER BY sal DESC
LIMIT 3;

# 급여 4 ~ 8위 출력
SELECT ename, sal
FROM emp
ORDER BY sal DESC
LIMIT 4 OFFSET 3;
```
