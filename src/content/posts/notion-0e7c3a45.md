---
title: "AI & 기계학습 기초"
publishedAt: 2026-08-05
---
<!-- notion-import-source: notion-export-0e7c3a4545af46449c81fdc6b064d476 -->

## AI, ML, DL

AL의 부분집합 ML, ML의 부분집합 DL

![image.png](/images/notion-0e7c3a45/image.png)

AI: 주어진 환경/데이터를 인지or학습or추론을 통해 목표 달성을 하도록 예측 행동선택 계획하는 시스템
ML: AI범주 내에서 데이터로부터 **학습**하여 목적을 달성하는 접근 방법론
DL: NN을 여러 층으로 깊게 구성하여 학습하는 방법론

## 데이터의 구성요소

| Feature | 데이터의 특성 |
| --- | --- |
| Lable | 분류 |

## AI 기초 개념

![image.png](/images/notion-0e7c3a45/image%201.png)

우리가 알고 싶은 결과(Y)는 입력 정보(X)에 어떤 규칙(f*)을 적용해서 만들어지고, 거기에 설명할 수 없는 오차(ε)가 조금 섞여 있다.
ε(엡실론)은 features로 설명되지 않는 부분을 의미함.

![image.png](/images/notion-0e7c3a45/image%202.png)

## 지도학습 : 처음 보는 문제도 잘 푸는 AI만들기

→ feature + label을 가지고 예측 규칙을 배우는 방법
목표: 훈련 데이터 뿐 아니라 처음 보는 데이터에서도 예측 성능 향상

## 지도학습이란?

→ 정답 라벨이 있는 훈련 데이터를 사용해 예측 모델을 학습하는 방법

## 회기 vs 분류

회기: 예측하고 싶은 결과값이 숫자
분류: 예측하고 싶은 결과값이 범주

## 손실 함수

## MSE (Mean Square Error) → 회귀

평균과 예측의 차이를 제곱해서 평균낸 값

![image.png](/images/notion-0e7c3a45/image%203.png)

## Cross Entropy → 분류

정답 범주에 얼마나 높은 확률을 주었는지 측정

![image.png](/images/notion-0e7c3a45/image%204.png)

## 회기 (Regression)

→ 입력(feature)으로부터 숫자(output)를 얼마나 정확히 예측할까?
→ 라벨 및 예측 모델의 출력은 연속적인 수치이다.

![image.png](/images/notion-0e7c3a45/image%205.png)

## 회기 오류: MSE

## 결정계수 R^2

![image.png](/images/notion-0e7c3a45/image%206.png)

→ 평균만 쓰는 단순한 예츨보다 얼마나 이 모델이 나음?
→ 1에 가까울수록 설명력이 높다
→ 음수이면 ‘차라리 평균이 나았네’

![image.png](/images/notion-0e7c3a45/image%207.png)

ex) MSE = (1000만원)^2 이면 좋은 성능의 모델임? R^2 = 0.8 은 좋은 모델임?

![image.png](/images/notion-0e7c3a45/image%208.png)

## 분류 (Classification)

→ Feature로부터 출력이 범주값(카테고리)로 나타나는 문제

![image.png](/images/notion-0e7c3a45/image%209.png)

## 정확도 (Accuracy)

![image.png](/images/notion-0e7c3a45/image%2010.png)

전체 예측 중에서 올바르게 맞춘 예측의 비율

### 정확도의 한계: 뷸균형 데이터 문제

양성 1%, 음성99%에서는 모두 음성이라 해도 정확도가 99%임.
→ 다른 지표도 봐야 안전하다

## 다른 지표: 혼동행렬

![image.png](/images/notion-0e7c3a45/image%2011.png)

Type1 error: 구라를 진짜로 믿음 (음성을 양성으로 판단)
Type2 error: 진짜를 구라로 믿음 (양성을 음성으로 판단)

### Percision

양성이라 판단한것 중 진짜 양성 비율
TP/(TP + FP)

### Sensitivity (Recall)

진짜 양성 가운데 잡아낸 예측 양성 비율
TP/(TP + FN)

### F1 - Score

![image.png](/images/notion-0e7c3a45/image%2012.png)

정밀도와 재현율의 조화평균

### Cross Entropy

![image.png](/images/notion-0e7c3a45/image%2013.png)

## Machine Learning

## 훈련 오류 vs 테스트 오류

![image.png](/images/notion-0e7c3a45/image%2014.png)

둘다 error가 높은 경우는 underfitting, training sample만 error가 낮은 경우는 overfitting

## Resampling

## Validation Set

데이터 순서를 무작위로 섞고 훈련셋, 검증셋으로 분할. 학습은 훈련셋이서, 성능 평가는 검증셋K에서.

## K-fold Corss Validation

데이터를 셔플링한 뒤, **겹치지 않는** K개 그룹으로 분할
각 그룹이 번갈아 검증셋, 나머지는 훈련셋

![image.png](/images/notion-0e7c3a45/image%2015.png)

### K-fold 교차검증 오류 계산

![image.png](/images/notion-0e7c3a45/image%2016.png)

![image.png](/images/notion-0e7c3a45/image%2017.png)

![image.png](/images/notion-0e7c3a45/image%2018.png)

CV는 결국 각 fold의 MSE의 가중평균

### Leave - One - Out

총 n개의 데이터를 n개의 fold로 나눠 K-fold Validation (즉, 매번 검증셋의 크기가 1임)

## 비지도학습

라벨이 없이 입력만으로 구조를 학습하는 기계학습방법론

ex) 클러스터링

## 클러스터링

→ 데이터 안에서 하위 집단(클러스터)을 찾는 기법들의 총칭

집단 내부는 서로 유사하게, 집단 간은 상이하도록 데이터 분할

- K-means → 클러스터 수(K)를 미리 정해놓고 분할하기
- Hirarchical → 클러스터 수 정하지 않음

## K-means Clustering

전체 데이터를 K개의 클러스터로 군집화하기

![image.png](/images/notion-0e7c3a45/image%2019.png)

하나의 데이터 포인트는 여러 그룹에 속할 수 없다.
하나의 데이터는 반드시 하나의 그룹에 속해 있다.

<aside>
💡

좋은 군집화 = 클러스터 내부변동이 작은 분할

</aside>

알고리즘 과정

1. 초기화
    
    관측치들에게 무작위로 1…K 클러스터 임시 부여
    
2. 반복
    1. 각 클러스터의 중심(centroid) 계산
    2. 각 관측치를 가장 가까운 중심의 클러스터에 재할당 (ex 유클리드 거리)

![image.png](/images/notion-0e7c3a45/image%2020.png)

초기화할때마다 결과가 다르기 때문에 여러 번 시도해봐야 

## Hierarchical Clustering

덴드로그램에서 수평선 높이(거리)를 기준으로 가위질하여 K개의 군집을 얻음

![image.png](/images/notion-0e7c3a45/image%2021.png)

→ 몇 개의 클러스터로 나눌지 사후에 나눌 수 있음

![image.png](/images/notion-0e7c3a45/image%2022.png)

![image.png](/images/notion-0e7c3a45/image%2023.png)

![image.png](/images/notion-0e7c3a45/image%2024.png)
