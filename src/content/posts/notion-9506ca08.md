---
title: "AI와 기계학습방법론"
publishedAt: 2026-08-06
---
<!-- notion-import-source: notion-export-9506ca08c92d466997c9c79a30fbb828 -->

## 단순선형회귀

하나의 설명변수(X)와 하나의 반응변수(Y) 사이의 선형(직선) 관계를 찾는 방법

→ 목표: 데이터를 가장 잘 설명하는 직선을 찾아 예측에 활용하기

모형 과정: $Y = \beta_0 + \beta_1X + \epsilon$

## 최소제곱법 (RSS)

→ 잔차(residual, e)를 제곱해 합한 값을 최소화하는 방법

$$
e_i = y_i - \hat y_i\newline
RSS = e_1^2 + e_2^2 + \cdots + e_n^2

$$

![image.png](/images/notion-9506ca08/image.png)

결과예시

![image.png](/images/notion-9506ca08/image%201.png)

## 다중선형회귀

→ 독립변수가 여러 개 존재할 떄 사용하는 회귀분석 기법

![image.png](/images/notion-9506ca08/image%202.png)

마찬가지로 RSS사용

행렬로도 표현 가능

![image.png](/images/notion-9506ca08/image%203.png)

![image.png](/images/notion-9506ca08/image%204.png)

그니까 선형회기는 그냥 계수 싹다 때려박아서 최적 기울기를 바로 구할 수 있음

결과 예시

![image.png](/images/notion-9506ca08/image%205.png)

TV, 라디오는 좀 유의함. 근데 신문 광고는 유의하지 않음

## 회귀의 주의점

→ 회귀는 ‘상관관계’를 설명하는거지 ‘인과관계’를 설명하는건 아님.

ex) 아이스크림 소비량: X, 상어에 물리는 사건: Y
하나도 관련없는 사건이 양의 상관관계를 띌 수 있다.

## Logistic Regerssion

![image.png](/images/notion-9506ca08/image%206.png)

![image.png](/images/notion-9506ca08/image%207.png)

시그모이드 함수에 

$$
z = \frac{e^z}{1+e^z}
$$

에다가

$$
z = \beta_0 + \beta_1 x
$$

를 대입하면 로지스틱 회귀 모형식이 됨

## Likelihood (우도)

→ 내 모형이 데이터를 잘 설명하는 정도 : 최대화해야한다. (Maximum Likelihood Estimation, MLE)

![image.png](/images/notion-9506ca08/image%208.png)

실제 데이터가 1인 애들을 싹다 모아서 예측값을 곱하고 (최대한 1이였으면 좋겠지?)
실제 데이터가 0인 애들을 싹다 모아서 1 - 예측값을 곱함 (얘네들도 최대한 1이였으면 좋겠음)
그니까 우도함수가 1에 가까울수록 예측을 잘한거임

근데 이대로 쓰면 미분이 거지같음 ㅇㅇ

![image.png](/images/notion-9506ca08/image%209.png)

양변에 로그 취해서 문제 해결

결과 예시

![image.png](/images/notion-9506ca08/image%2010.png)

balance 계수가 진짜 쪼그만데 그럼에도 얘는 sigmoid하게 증가하는 애들이라, 얕보면 안됨
특정 구간에서 예측 확률값이 엄청 크게 증가할 수 있기 때문

![image.png](/images/notion-9506ca08/image%2011.png)

얘도 다중 feature 회기 당연 가능하다. 

z-statistic은 t-statistics랑 사실상 똑같음 ㅇㅇ

## Shallow Network

Input - Hidden layer - Output : 즉 은닉층이 딱 1개임

![image.png](/images/notion-9506ca08/image%2012.png)

모수: 학습해야하는 대상

a[ ] : 활성함수 (예시: ReLU)

![image.png](/images/notion-9506ca08/image%2013.png)

→ 0이하의 수가 나오면 꺼주자. (0을 뱉어주자)

## Shallow Network: piecewise linear function

![image.png](/images/notion-9506ca08/image%2014.png)

→ 구간별로 선형 함수임. 활성함수가 꺾인 부분(비선형성)을 만든다.

![image.png](/images/notion-9506ca08/image%2015.png)

![image.png](/images/notion-9506ca08/image%2016.png)

![image.png](/images/notion-9506ca08/image%2017.png)

일차식이 있음
그걸 활성함수에 때려박음
그게 여려개있음
그걸 싹다 더해버림
→ 네트워크 만들어짐

![image.png](/images/notion-9506ca08/image%2018.png)

인풋 아웃풋 늘리면 요래 됨

## Deep Network

왜 Deep?

![image.png](/images/notion-9506ca08/image%2019.png)

표현력이 훨씩 굳임

![image.png](/images/notion-9506ca08/image%2020.png)

변수가 너무 많으니까 좀 쉽게 줄이자.

GG~~~

## Gradient Descent

손실함수를 최소화하기 위해 파라미터를 반복적으로 갱신하는 알고리즘
→ 기울기(미분값)의 반대 방향으로 이동해야 손실 함수가 줄어듬

![image.png](/images/notion-9506ca08/image%2021.png)

여기서 알파는 학습률, 한 번의 스텝에서 이동하는 크기 결정

## Convex vs Non-convex

convex

→ 곡선이 항상 U자처럼 아래로 볼록함. 그래프 위 임의 두 점을 잇는 직선이 그래프 위로 있음

non-convex

→봉우리와 골짜기가 섞인 모양. 두 점을 이은 직선이 그래프 아래로 내려가는 구간이 생김

![image.png](/images/notion-9506ca08/image%2022.png)

![image.png](/images/notion-9506ca08/image%2023.png)

## 확률적 경사 하강법 (Stochastic gradient descent)

→ 우리가 볼 많은 함수는 거의 non-convex함수임.
local minimum에 빠질 가능성이 크고, 한 번 빠지면 또 나오기도 어려움

무작위 확률로 샘플된 일부 데이터(batch)에서만 경사하강법 사용

![image.png](/images/notion-9506ca08/image%2024.png)

- 미분 경로의 무작위성
- 노이즈가 있지만 여전히 타당한 업데이트 → saddle point, local min 탈출
- 계산 비용 절감
- 매끄럽지 않고 지그재그하게 수렴한다

## 역전파 (Backpropagation)

→ Layer별로 파라미터들이 존재해서 서로 영향을 미치는데, 미분을 어케함?

## 합성함수의 미분: 연쇄법칙

![image.png](/images/notion-9506ca08/image%2025.png)

![image.png](/images/notion-9506ca08/image%2026.png)

## 역전파란?

출력 오차 기준으로 그래프를 거꾸로 따라가며 연쇄법칙으로 각 노드의 미분값을 계산하는 절차

! : depth가 깊어지면 표현력이 증가함.
근데 역전파에서 미분값 구하려면 계산량이 너무 많아져서 학습이 어려워짐
trade off, no free lunch

GG~

[Ch.1-2_004_MLP 모델 구현 및 학습.ipynb](/files/notion-9506ca08/Ch.1-2_004_MLP_%EB%AA%A8%EB%8D%B8_%EA%B5%AC%ED%98%84_%EB%B0%8F_%ED%95%99%EC%8A%B5.ipynb)

[Ch.1-2_004_MLP 모델 구현 및 학습 (1).ipynb](Ch.1-2_004_MLP_%EB%AA%A8%EB%8D%B8_%EA%B5%AC%ED%98%84_%EB%B0%8F_%ED%95%99%EC%8A%B5_(1).ipynb)

[Ch.1-2_005_결정 경계 시각화 (1).ipynb](Ch.1-2_005_%EA%B2%B0%EC%A0%95_%EA%B2%BD%EA%B3%84_%EC%8B%9C%EA%B0%81%ED%99%94_(1).ipynb)

[Ch.1-2_005_결정 경계 시각화.ipynb](/files/notion-9506ca08/Ch.1-2_005_%EA%B2%B0%EC%A0%95_%EA%B2%BD%EA%B3%84_%EC%8B%9C%EA%B0%81%ED%99%94.ipynb)
