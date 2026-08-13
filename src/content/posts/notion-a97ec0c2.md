---
title: "6. Generic"
publishedAt: 2026-07-28
---
<!-- notion-import-source: notion-export-a97ec0c22a1046c18edcea6dcda34d45 -->

## Wraper Class

```java
public class BoxTest {
	public static void main(String args[]) {
		
		//Wrapper class
		Byte b;
		Short s;
		Integer i;
		Long l;
		Boolean bb;
		Character c;
		Float f;
		Double d;
		
		int i1 = 10; //객체 아님
		Integer i2 = 10; //객체임 (Auto Boxing)
		Integer i3 = Integer.valueOf(i1); //객체임
		int i4 = i2; //객체 아님 (Auto Unboxing)
		int i5 = i3.intValue();
	}
}
```

Primitive data type을 Reference type로 바꿈

## Generic

→ 데이터 타입을 나중에 결정하겠다

```java
package generics_01_normal_box;

//직접 박스 내용물을 지정한 박스
class Box<T>{
	private T obj;

	public T getObj() {
		return obj;
	}

	public void setObj(T obj) {
		this.obj = obj;
	}
}

public class BoxTest {
	public static void main(String args[]) {
		
//		Box box = new Box(); //Object가 자동으로 들어간다 -> 비권장
		
		Box<String> stringBox1 = new Box<String>(); //정석적 활용
		Box<String> stringBox2 = new Box<>(); //정석적 활용
		
		stringBox1.setObj("문자열");
//		stringBox2.setObj(1000); //못넣어용
		
		System.out.println(stringBox1.getObj());
	}
}
```

## Generic method

~~흐린눈~~

→ Type parameter를 사용하는 메서드

## 한정 타입 매개변수

## Wildcard
