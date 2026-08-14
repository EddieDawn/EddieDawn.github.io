---
title: "딥러닝 및 이미지 모델"
publishedAt: 2026-08-14
---
<!-- notion-import-source: notion-export-b23c63098d0043d5b11407d7e31e5eec -->

## CNN 살펴보기

## CNN vs FCN

### FCN

입력을 받아서 출력으로 변환하는 신경망의 기본 모듈
ex) number mnist dataset

### Convolution Layer

- 입력 이미지를 필터와 연산하여 특징 맵(feature map)을 뽑아내는 모듈
- 1차원 구조로 변환하는 FCN과 달리 3차원 구조를 그대로 보존하면서 연산
- Conlolution: 필터를 이미지 상에서 이동시키면서 내적을 반복 수행

![image.png](/images/notion-b23c6309/image.png)

![image.png](/images/notion-b23c6309/image%201.png)

→ 입력 대비 출력의 공간 해상도가 줄어듦
→ 츨력 해상도는 입력 해상도 - 필터 해상도 + 1로 도출

## 모델 구조

### 중첩

그냥 상수만 증가시키면 결국 상수 하나를 곱한거랑 똑같아짐. (선형변환을 여러번하면 그냥 선형임)
그래서 비선형 블록(ReLU와 같은)과 함께하면 모델링 파워 향상

![image.png](/images/notion-b23c6309/image%202.png)

### 필터 시각화

학습된 필터 시각화를 통해 각 모델(구조)이 학습한 정보를 이해 가능

![image.png](/images/notion-b23c6309/image%203.png)

### 수용 영역

: CNN이 이미지를 처리하면서 한 번에 볼 수 있는 영역의 크기, 즉 네트워크의 시야

### 중첩과 수용영역

![image.png](/images/notion-b23c6309/image%204.png)

### 풀링

![image.png](/images/notion-b23c6309/image%205.png)

CNN레이어 출력을 줄여 연산 효율성 확보 & 위치 변화 강건성 증가

### 스트라이드 합성곱

필터를 스트라이드 값만큼(S값) 이동한 후 출력 연산.
중간중간 건너뛰며 필터 연산을 진행하이 마치 풀링을 진행한 것 처럼 연산함 (데이터 손실은 없이)

![image.png](/images/notion-b23c6309/image%206.png)

필터를 한 칸이 아닌 두 칸씩 건너뛰는 모습

## CNN 기반 모델 변천사

## AlexNet

## VGGNet

## ResNet

## MobileNet
