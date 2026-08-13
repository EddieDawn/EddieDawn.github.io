---
title: "파이썬 - 데이터 다루기"
publishedAt: 2026-08-04
---
<!-- notion-import-source: notion-export-2aa08514452742e5a86806b4f80817ee -->

## Numpy

![image.png](/images/notion-2aa08514/image.png)

→ 수학 및 과학을 위한 파이썬 패키지
     리스트의 덧셈, 곱셉과 같은 연산을 더 직관적으로 만들어줌

## Numpy 배열의 특징

| 배열 (ndarray) | 같은 자료형의 데이터를 담는 다차원 자료구조 |
| --- | --- |
| 벡터화 (Vectorization) | 반복문 없이 배열 전체에 연산 적용 |
| 연산 속도 | 반복문보다 빠름 |
| 집계 함수 | mean, sum, max, min, std |

![image.png](/images/notion-2aa08514/image%201.png)

![download.png](/images/notion-2aa08514/download.png)

![image.png](/images/notion-2aa08514/image%202.png)

![download.png](/images/notion-2aa08514/download%201.png)

## Reshape과 축 연산

## Broadcasting

크기가 다른 배열을 연산할 수 있도록 배열의 형태를 동적으로 변환

## 조건부 필터링

## 정렬

## Pandas

![image.png](/images/notion-2aa08514/image%203.png)

![image.png](/images/notion-2aa08514/image%204.png)

![download.png](/images/notion-2aa08514/download%202.png)

![download.png](/images/notion-2aa08514/download%203.png)

![download.png](/images/notion-2aa08514/download%204.png)

## Groupby 집계

![download.png](/images/notion-2aa08514/download%205.png)

```python
# 1. 매출 상위 5개 주문을 상위5 에 할당해 주세요.
상위5 = df.nlargest(5,"매출")
assert len(상위5) == 5 and 상위5["매출"].iloc[0] == df["매출"].max(), "nlargest 결과가 올바르지 않습니다."

# 2. 수량 하위 3개 주문을 하위3 에 할당해 주세요.
하위3 = df.nsmallest(3, "수량")
assert len(하위3) == 3 and 하위3["수량"].max() <= df["수량"].min() + 1, "nsmallest 결과가 올바르지 않습니다."

# 3. 부산 지역의 매출 컬럼만 골라 부산매출 에 할당해 주세요.
부산매출 = df.loc[df["지역"] == "부산", "매출"]
assert isinstance(부산매출, pd.Series) and len(부산매출) == (df["지역"] == "부산").sum(), "loc 선택이 올바르지 않습니다."

# 4. 0행 0열의 값을 첫값 에 할당해 주세요. (위치 기반)
첫값 = df.iloc[0, 0]
assert 첫값 == df["지역"].iloc[0], "iloc 선택이 올바르지 않습니다."

# 5. 사본 df3 에서 단가가 4500 미만인 행의 단가를 4500 으로 올려 주세요. (조건부 대입)
df3 = df.copy()
df3.loc[df3["단가"] < 4500, "단가"] = 4500
assert df3["단가"].min() == 4500, "조건부 대입이 올바르지 않습니다."

print("TODO 7 통과!")
```
