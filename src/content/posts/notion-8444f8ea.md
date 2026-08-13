---
title: "7. Collection Framework"
publishedAt: 2026-07-28
---
<!-- notion-import-source: notion-export-8444f8ea2b3a4fbcb453beca1f291aa8 -->

## Collection Framework

- 데이터를 동적 크기로 관리
- 삽입, 삭제, 검색, 정렬이 효율적임
- 제네릭 활용 → 타입 안정성 Good
- 표준화된 메서드 제공

![image.png](/images/notion-8444f8ea/image.png)

## List

- 순서 있는 데이터 집합
- 중복데이터 허용
- 구현 클래스
    - ArrayList
    - LinkedList
    - ~~Vector~~

## ArrayList

- 배열 기반 / 인덱스로 접근
- 조회가 많고 삽입 / 삭제가 적은 경우 Good

## LinkedList

- 노드 기반 구현 / 참조로 접근
- 조회가 적고 삽입 / 삭제가 많은 경우 Good

### List계열 메서드 모음

![image.png](/images/notion-8444f8ea/image%201.png)

## Set

- 순서 X
- 중복 X
- null값 허용
- 데이터 고유성 보장
    - HashSet
    - LinkedHashSet
    - TreeSet

## HashSet

- HashMap 기반으로 동작
- null값은 하나만 저장 가능

## LinkedHashSet

- 데이터 저장 순서 유지
- LinkedHashMap 기반 동작
- 이중 Linked List

## TreeSet

### Set 계열 메서드

![image.png](/images/notion-8444f8ea/image%202.png)

## Map

→ Key, Value를 쌍으로 데이터 저장

## HashMap

- 내부적으로 Hash Table을 사용

## LinkedHashMap

## TreeMap

### Map계열 메서드

![image.png](/images/notion-8444f8ea/image%203.png)

## Sort

배열은 Arrays.sort()이용

콜렉션은 Collections.sort() 이용

## Comparable인터페이스

→ 객체의 기본 정렬 기준을 정의 (클래스에 직접 구현)

```java
public interface Comarable<T>{
	public int compareTo(T o);
}
```
