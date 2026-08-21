---
title: "AI와 기계학습방법론"
publishedAt: 2026-08-06
---
<!-- notion-import-source: notion-page-3b4154b95f6780f795e2feefb465dc12 -->

## 단순선형회귀

하나의 설명변수(X)와 하나의 반응변수(Y) 사이의 선형(직선) 관계를 찾는 방법

![image.png](/images/AI%EC%99%80%20%EA%B8%B0%EA%B3%84%ED%95%99%EC%8A%B5%EB%B0%A9%EB%B2%95%EB%A1%A0/image.png)

![image.png](/images/AI%EC%99%80%20%EA%B8%B0%EA%B3%84%ED%95%99%EC%8A%B5%EB%B0%A9%EB%B2%95%EB%A1%A0/image%201.png)

→ 목표: 데이터를 가장 잘 설명하는 직선을 찾아 예측에 활용하기

## 최소제곱법 (RSS)

→ 잔차(residual, e)를 제곱해 합한 값을 최소화하는 방법

![image.png](/images/AI%EC%99%80%20%EA%B8%B0%EA%B3%84%ED%95%99%EC%8A%B5%EB%B0%A9%EB%B2%95%EB%A1%A0/image%202.png)

![image.png](/images/AI%EC%99%80%20%EA%B8%B0%EA%B3%84%ED%95%99%EC%8A%B5%EB%B0%A9%EB%B2%95%EB%A1%A0/image%203.png)

e_i는 잔차(residual)이라고 함.

![image.png](/images/AI%EC%99%80%20%EA%B8%B0%EA%B3%84%ED%95%99%EC%8A%B5%EB%B0%A9%EB%B2%95%EB%A1%A0/image%204.png)

결과예시

![image.png](/images/AI%EC%99%80%20%EA%B8%B0%EA%B3%84%ED%95%99%EC%8A%B5%EB%B0%A9%EB%B2%95%EB%A1%A0/image%205.png)

## 다중선형회귀

→ 독립변수가 여러 개 존재할 떄 사용하는 회귀분석 기법

![image.png](/images/AI%EC%99%80%20%EA%B8%B0%EA%B3%84%ED%95%99%EC%8A%B5%EB%B0%A9%EB%B2%95%EB%A1%A0/image%206.png)

마찬가지로 RSS사용

행렬로도 표현 가능

![image.png](/images/AI%EC%99%80%20%EA%B8%B0%EA%B3%84%ED%95%99%EC%8A%B5%EB%B0%A9%EB%B2%95%EB%A1%A0/image%207.png)

![image.png](/images/AI%EC%99%80%20%EA%B8%B0%EA%B3%84%ED%95%99%EC%8A%B5%EB%B0%A9%EB%B2%95%EB%A1%A0/image%208.png)

그니까 선형회기는 그냥 계수 싹다 때려박아서 최적 기울기를 바로 구할 수 있음

결과 예시

![image.png](/images/AI%EC%99%80%20%EA%B8%B0%EA%B3%84%ED%95%99%EC%8A%B5%EB%B0%A9%EB%B2%95%EB%A1%A0/image%209.png)

![image.png](/images/AI%EC%99%80%20%EA%B8%B0%EA%B3%84%ED%95%99%EC%8A%B5%EB%B0%A9%EB%B2%95%EB%A1%A0/image%2010.png)

TV, 라디오는 좀 유의함. 근데 신문 광고는 유의하지 않음

## 회귀의 주의점

→ 회귀는 ‘상관관계’를 설명하는거지 ‘인과관계’를 설명하는건 아님.

ex) 아이스크림 소비량: X, 상어에 물리는 사건: Y
하나도 관련없는 사건이 양의 상관관계를 띌 수 있다.

## Logistic Regerssion (이름은 회귀지만 분류임ㅋㅋ)

![image.png](/images/AI%EC%99%80%20%EA%B8%B0%EA%B3%84%ED%95%99%EC%8A%B5%EB%B0%A9%EB%B2%95%EB%A1%A0/image%2011.png)

![image.png](/images/AI%EC%99%80%20%EA%B8%B0%EA%B3%84%ED%95%99%EC%8A%B5%EB%B0%A9%EB%B2%95%EB%A1%A0/image%2012.png)

시그모이드 함수

![image.png](/images/AI%EC%99%80%20%EA%B8%B0%EA%B3%84%ED%95%99%EC%8A%B5%EB%B0%A9%EB%B2%95%EB%A1%A0/image%2013.png)

에다가 선형회귀식인

![image.png](/images/AI%EC%99%80%20%EA%B8%B0%EA%B3%84%ED%95%99%EC%8A%B5%EB%B0%A9%EB%B2%95%EB%A1%A0/image%2014.png)

를 대입하면 

![image.png](/images/AI%EC%99%80%20%EA%B8%B0%EA%B3%84%ED%95%99%EC%8A%B5%EB%B0%A9%EB%B2%95%EB%A1%A0/image%2015.png)

로지스틱 회귀 모형식이 됨

![image.png](/images/AI%EC%99%80%20%EA%B8%B0%EA%B3%84%ED%95%99%EC%8A%B5%EB%B0%A9%EB%B2%95%EB%A1%A0/image%2016.png)

## Likelihood (우도)

→ 내 모형이 데이터를 잘 설명하는 정도 : 최대화해야한다. (Maximum Likelihood Estimation, MLE)

![image.png](/images/AI%EC%99%80%20%EA%B8%B0%EA%B3%84%ED%95%99%EC%8A%B5%EB%B0%A9%EB%B2%95%EB%A1%A0/image%2017.png)

실제 데이터가 1인 애들을 싹다 모아서 예측값을 곱하고 (최대한 1이였으면 좋겠지?)
실제 데이터가 0인 애들을 싹다 모아서 1 - 예측값을 곱함 (얘네들도 최대한 1이였으면 좋겠음)
그니까 우도함수가 1에 가까울수록 예측을 잘한거임

근데 이대로 쓰면 미분이 쉽지않음

![image.png](/images/AI%EC%99%80%20%EA%B8%B0%EA%B3%84%ED%95%99%EC%8A%B5%EB%B0%A9%EB%B2%95%EB%A1%A0/image%2018.png)

양변에 로그 취해서 문제 해결 (log-likelyhood)

결과 예시

![image.png](/images/AI%EC%99%80%20%EA%B8%B0%EA%B3%84%ED%95%99%EC%8A%B5%EB%B0%A9%EB%B2%95%EB%A1%A0/image%2019.png)

balance 계수가 진짜 쪼그만데 그럼에도 얘는 sigmoid하게 증가하는 애들이라, 얕보면 안됨
특정 구간에서 예측 확률값이 엄청 크게 증가할 수 있기 때문

![image.png](/images/AI%EC%99%80%20%EA%B8%B0%EA%B3%84%ED%95%99%EC%8A%B5%EB%B0%A9%EB%B2%95%EB%A1%A0/image%2020.png)

얘도 다중 feature 회기 당연 가능하다. 

z-statistic은 t-statistics랑 사실상 같은 의미로 봐도 된다

## Shallow Network

Input - Hidden layer - Output : 즉 은닉층이 딱 1개임

![image.png](/images/AI%EC%99%80%20%EA%B8%B0%EA%B3%84%ED%95%99%EC%8A%B5%EB%B0%A9%EB%B2%95%EB%A1%A0/image%2021.png)

모수: 학습해야하는 대상

a[ ] : 활성함수 (예시: ReLU)

![image.png](/images/AI%EC%99%80%20%EA%B8%B0%EA%B3%84%ED%95%99%EC%8A%B5%EB%B0%A9%EB%B2%95%EB%A1%A0/image%2022.png)

→ 0이하의 수가 나오면 꺼주자. (0을 뱉어주자)

## Shallow Network: piecewise linear function

![image.png](/images/AI%EC%99%80%20%EA%B8%B0%EA%B3%84%ED%95%99%EC%8A%B5%EB%B0%A9%EB%B2%95%EB%A1%A0/image%2023.png)

→ 구간별로 선형 함수임. 활성함수가 꺾인 부분(비선형성)을 만든다.

![image.png](/images/AI%EC%99%80%20%EA%B8%B0%EA%B3%84%ED%95%99%EC%8A%B5%EB%B0%A9%EB%B2%95%EB%A1%A0/image%2024.png)

![image.png](/images/AI%EC%99%80%20%EA%B8%B0%EA%B3%84%ED%95%99%EC%8A%B5%EB%B0%A9%EB%B2%95%EB%A1%A0/image%2025.png)

![image.png](/images/AI%EC%99%80%20%EA%B8%B0%EA%B3%84%ED%95%99%EC%8A%B5%EB%B0%A9%EB%B2%95%EB%A1%A0/image%2026.png)

![image.png](/images/AI%EC%99%80%20%EA%B8%B0%EA%B3%84%ED%95%99%EC%8A%B5%EB%B0%A9%EB%B2%95%EB%A1%A0/image%2027.png)

일차식이 있음
h_1, h_2, h_3에 일차식이 있음. (계수와 편향). 계산함.
그걸 활성함수에 때려박음
그게 여려개있음
그걸 싹다 더해버림 (편향도 더해지긴 함)
→ 네트워크 만들어짐

## 다중 입/출력

input feature가 하나가 아니라 두 개면 shallow network의 모양은 다음과 같다

![image.png](/images/AI%EC%99%80%20%EA%B8%B0%EA%B3%84%ED%95%99%EC%8A%B5%EB%B0%A9%EB%B2%95%EB%A1%A0/image%2028.png)

이를 시각화해보자면 (위 예시는 feature가 2개, 아래는 3개이긴 함. 같은 식은 아님)

![image.png](/images/AI%EC%99%80%20%EA%B8%B0%EA%B3%84%ED%95%99%EC%8A%B5%EB%B0%A9%EB%B2%95%EB%A1%A0/image%2029.png)

![image.png](/images/AI%EC%99%80%20%EA%B8%B0%EA%B3%84%ED%95%99%EC%8A%B5%EB%B0%A9%EB%B2%95%EB%A1%A0/image%2030.png)

![image.png](/images/AI%EC%99%80%20%EA%B8%B0%EA%B3%84%ED%95%99%EC%8A%B5%EB%B0%A9%EB%B2%95%EB%A1%A0/image%2031.png)

이런식임

총 정리하자면

![image.png](/images/AI%EC%99%80%20%EA%B8%B0%EA%B3%84%ED%95%99%EC%8A%B5%EB%B0%A9%EB%B2%95%EB%A1%A0/image%2032.png)

## Deep Network

왜 Deep?

![image.png](/images/AI%EC%99%80%20%EA%B8%B0%EA%B3%84%ED%95%99%EC%8A%B5%EB%B0%A9%EB%B2%95%EB%A1%A0/image%2033.png)

표현력이 훨씩 굳임

![image.png](/images/AI%EC%99%80%20%EA%B8%B0%EA%B3%84%ED%95%99%EC%8A%B5%EB%B0%A9%EB%B2%95%EB%A1%A0/image%2034.png)

변수가 너무 많으니까 좀 쉽게 줄이자.
계산식을 하나하나 줄이는걸 다 외우는건 필요도 없고 요구받지도 않는다.

다만 알아야 할 것:
첫 번째 Layer의 모든 노드가 두 번째 Layer의 노드와 연결된다 → Fully connected

![image.png](/images/AI%EC%99%80%20%EA%B8%B0%EA%B3%84%ED%95%99%EC%8A%B5%EB%B0%A9%EB%B2%95%EB%A1%A0/image%2035.png)

오메가는 weight matrix
D는 차원 수
베타는 바이어스 matrix

## 손실함수

![image.png](/images/AI%EC%99%80%20%EA%B8%B0%EA%B3%84%ED%95%99%EC%8A%B5%EB%B0%A9%EB%B2%95%EB%A1%A0/image%2036.png)

내가 예측한 값이 현 파라미터에 대해 실제 레이블과 얼마나 틀렸나?
데이터 → 고정되어있음
예측값은? 파라미터(psi)값에 의해 바뀜.

즉, 이를 줄여 말하면

![image.png](/images/AI%EC%99%80%20%EA%B8%B0%EA%B3%84%ED%95%99%EC%8A%B5%EB%B0%A9%EB%B2%95%EB%A1%A0/image%2037.png)

그냥 이거다. 파라미터 하나에만 의존하여 손실함수 값이 바뀐다.
즉 학습이란? 손실함수를 최소화시키는 파라미터 찾기 그 자체임

![image.png](/images/AI%EC%99%80%20%EA%B8%B0%EA%B3%84%ED%95%99%EC%8A%B5%EB%B0%A9%EB%B2%95%EB%A1%A0/image%2038.png)

## Gradient Descent

손실함수를 최소화하기 위해 파라미터를 반복적으로 갱신하는 알고리즘
→ 기울기(미분값)의 반대 방향으로 이동해야 손실 함수가 줄어듬

![image.png](/images/AI%EC%99%80%20%EA%B8%B0%EA%B3%84%ED%95%99%EC%8A%B5%EB%B0%A9%EB%B2%95%EB%A1%A0/image%2039.png)

![image.png](/images/AI%EC%99%80%20%EA%B8%B0%EA%B3%84%ED%95%99%EC%8A%B5%EB%B0%A9%EB%B2%95%EB%A1%A0/image%2040.png)

여기서 알파는 학습률, 한 번의 스텝에서 이동하는 크기 결정

## Convex vs Non-convex

convex

→ 곡선이 항상 U자처럼 아래로 볼록함. 그래프 위 임의 두 점을 잇는 직선이 그래프 위로 있음

non-convex

→봉우리와 골짜기가 섞인 모양. 두 점을 이은 직선이 그래프 아래로 내려가는 구간이 생김

![image.png](/images/AI%EC%99%80%20%EA%B8%B0%EA%B3%84%ED%95%99%EC%8A%B5%EB%B0%A9%EB%B2%95%EB%A1%A0/image%2041.png)

![image.png](/images/AI%EC%99%80%20%EA%B8%B0%EA%B3%84%ED%95%99%EC%8A%B5%EB%B0%A9%EB%B2%95%EB%A1%A0/image%2042.png)

## 확률적 경사 하강법 (Stochastic gradient descent)

→ 우리가 볼 많은 함수는 거의 non-convex함수임.
local minimum에 빠질 가능성이 크고, 한 번 빠지면 또 나오기도 어려움

무작위 확률로 샘플된 일부 데이터(batch)에서만 경사하강법 사용

![image.png](/images/AI%EC%99%80%20%EA%B8%B0%EA%B3%84%ED%95%99%EC%8A%B5%EB%B0%A9%EB%B2%95%EB%A1%A0/image%2043.png)

![image.png](/images/AI%EC%99%80%20%EA%B8%B0%EA%B3%84%ED%95%99%EC%8A%B5%EB%B0%A9%EB%B2%95%EB%A1%A0/image%2044.png)

- 미분 경로의 무작위성
- 노이즈가 있지만 여전히 타당한 업데이트 → 오히려 saddle point, local min 탈출에 도움을 줌
- 계산 비용 절감
- 매끄럽지 않고 지그재그하게 수렴한다

## 역전파 (Backpropagation)

→ Layer별로 파라미터들이 존재해서 서로 영향을 미치는데, 미분을 어케함?

## 역전파란?

모델이 틀린 정도를 보고, 각 가중치(파라미터)가 그 오답에 얼마나 책임이 있는지 뒤에서부터 계산하는 과정출력 오차 기준으로 그래프를 거꾸로 따라가며 연쇄법칙으로 각 노드의 미분값을 계산하는 절차

! : depth가 깊어지면 표현력이 증가함.
근데 역전파에서 미분값 구하려면 계산량이 너무 많아져서 학습이 어려워짐
trade off, no free lunch

그니까 엄청 복잡한 식을 거꾸로(반대 방향으로) 미분하여 파라미터를 찾아내는 과정을 말함.

![image.png](/images/AI%EC%99%80%20%EA%B8%B0%EA%B3%84%ED%95%99%EC%8A%B5%EB%B0%A9%EB%B2%95%EB%A1%A0/image%2045.png)

![image.png](/images/AI%EC%99%80%20%EA%B8%B0%EA%B3%84%ED%95%99%EC%8A%B5%EB%B0%A9%EB%B2%95%EB%A1%A0/image%2046.png)

![image.png](/images/AI%EC%99%80%20%EA%B8%B0%EA%B3%84%ED%95%99%EC%8A%B5%EB%B0%A9%EB%B2%95%EB%A1%A0/image%2047.png)

![image.png](/images/AI%EC%99%80%20%EA%B8%B0%EA%B3%84%ED%95%99%EC%8A%B5%EB%B0%A9%EB%B2%95%EB%A1%A0/image%2048.png)

![image.png](/images/AI%EC%99%80%20%EA%B8%B0%EA%B3%84%ED%95%99%EC%8A%B5%EB%B0%A9%EB%B2%95%EB%A1%A0/image%2049.png)
