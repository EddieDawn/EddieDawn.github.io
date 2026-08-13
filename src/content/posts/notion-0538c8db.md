---
title: "3. Java - Inheritance"
publishedAt: 2026-07-27
---
<!-- notion-import-source: notion-export-0538c8db6bcb42c39d4467bb14af67cb -->

## 상속이란?

## is - a VS has - a

## super();

→ 조상 클래스의 기본 생성자 호출하기 

## Obejct 클래스

→ 자바의 최상위 클래스

- Object.toString()
    
    → String.valueOf() 에서 호출됨
    
- Object.equals()
    
    → 같은 객체인가?
    
    → 값 비교를 위해선 오버라이딩 합시다.
    
- Object.hashCode()
    
    → HashSet, HashMap 등 객체 동일성 확인할 때 씀
    

<aside>
💡

equals()랑 hashcode()는 둘다 오버라이딩 해야해요

</aside>

## final

- final var
    
    → 값 변경이 필요없는 상수 선언.
    
    → UPPERCASE_SNAKE_CASE
    
- final method
    
    → @Overriding 불가
    
- final class
    
    → 상속할 수 없는 클래스 정의
    
    → ex) String 클래스는 final로 선언되어있음
    

## !Binding!

```java
class Parent {
    int value = 10;

    void print() {
        System.out.println("Parent Method");
    }
}

class Child extends Parent {
    int value = 20; // 멤버 변수 은닉 (Shadowing)

    @Override
    void print() {
        System.out.println("Child Method");
    } // 메서드 오버라이딩
}

public class Test {
    public static void main(String[] args) {
        // 업캐스팅 발생
        Parent obj = new Child();
        System.out.println(obj.value);
        obj.print();
    }
}
```

## Static Binding

→ 자바의 Variable은 컴파일 타임에 변수의 참조 타입을 보고 결정됨. Ploymorphism 적용  X

obj는 Parent객체로 선언됨. 따라서 10이 출력됨.

Child의 변수는 멤버 변수 은닉(Shadowing)됨.

## Dynamic Binding

→ 자바의 method는 런타임에 실제 instance가 무엇인지 보고 결정됨. Ploymorphism 적용  O

obj는 Parent로 선언되었지만 사실은 Child의 instance임.

따라서 Child의  print()가 호출됨.
