---
title: "언어 모델"
publishedAt: 2026-08-10
---
<!-- notion-import-source: notion-export-ec7a5661d8574bc299f4219db8a6be06 -->

## 단어를 숫자로 표현하기: 워드 임베딩

## 원 핫 인코딩

→ 단어를 원자적(쪼갤 수 없는) 기호로 취급함. 

문제점: 유사도 측정 불가

## 워드 임베딩

: 단어를 단어 사이의 의미적 관계를 포착할 수 있는 밀집되고 분산적 벡터 표현으로 나타내는 방법

### Skip-grams(SG): 중심 단어를 통해 주변 단어 예측하기

![image.png](/images/notion-ec7a5661/image.png)

### Continuous Bag of Words (CBOW): 주변 단어를 통해서 중심 단어 예측하기

![image.png](/images/notion-ec7a5661/image%201.png)

![image.png](/images/notion-ec7a5661/image%202.png)

## 언어는 순서가 중요하다: 순차적 데이터의 특징

## 순차적 데이터란?

→ 데이터가 입력되는 순서와 이 순서를 통해 입력되는 데이터들 사이의 관계가 중요한 데이터

ex) 오디오, 텍스트, 비디오 등

## 순차적 데이터의 특징

1. 순서가 중요하다
2. 장기 의존성 (Long-term dependency)
3. 가변 길이

## RNN: 문맥을 기억하는 신경망

→ 가변적인 길이의 입력을 받을 수 있고, 이전 입력을 기억할 수 있는 AI모델. 순차적 데이터 처리에 적합

![image.png](/images/notion-ec7a5661/image%203.png)

![image.png](/images/notion-ec7a5661/image%204.png)

### RNN의 한계: 기울기 소실(vanishing gradient)

Back propagation 시 앞쪽 층 기울기가 0에 가까워져서 장기 의존성 학습이 어려워지는 현상

## LSTM: 더 오래 기억하는 신경망

![image.png](/images/notion-ec7a5661/image%205.png)

→ 3가지 게이트를 통해 어떤 정보를 지우고, 쓰고, 읽을지 결정한다.

| Forget gate | 이전 cell state에서 무엇을 지우고 버릴지 결정 |
| --- | --- |
| Input gate | 새 정보 중 얼마나 쓸 것인지 결정 |
| Output gate | cell state중 얼마나 hidden state로 내보낼지 결정 |

## Forget gate

이전 cell state에서  무엇을 버리고 유지할지 결정

![image.png](/images/notion-ec7a5661/image%206.png)

## Input Gate

새 정보 중 얼마나 cell state에 쓸지 결정

![image.png](/images/notion-ec7a5661/image%207.png)

## Output Gate

cell state중 얼마나 hidden state로 내보낼지 결정

![image.png](/images/notion-ec7a5661/image%208.png)

## 언어모델이란?

: 인간의 두뇌가 자연어를 생성하는 능력을 모방한 모델

## N-gram model

n-gram이란?
→ 연속된 n개의 단어 묶음을 말한다.

다양한 n-gram이 얼마나 자주 등장하는지 통계를 수집하고 이를 통해 다음 단어Se 예측

## Seq2Seq

## Neural Machine Translation이란?

인공 신경망을 이용해 기계 번역을 수행하는 방법.
이 때 사용되는 신경망 구조를 sequence-to-sequence(Seq2Seq)라 하며, 두 개의 RNN으로 이루어짐

- 2개의 LSTM을 이용하자
    - 한 LSTM은 입력 시퀀스를 한 타임스텝씩 읽어 고정된 차원의 큰 벡터표현 얻기 (Encoder)
    - 다른 LSTM은 앞에서 얻은 벡터로부터 출력 시퀀스 생성하기 (Decoder)

Seq2Seq 모델은 인코더와 디코더가 하나의 통합 네트워크로 연결되어 있다.

- Teacher Forcing이란?
    - 모델이 스스로 예측한 단어 대신 정답 단어를 디코더 입력으로 강제주입 → 학습 가속
- Greedy Inference
    - 토큰을 출력하는 방법 중 하나로, 각 단계에서 가장 확률이 높은 단어 선택
    - 즉, 오답을 되돌리기가 불가능함
- Beam Search
    - 매 단계마다 k개의 가장 유망한 후보 유지
    - 후보다 EOS에 도달하면 완성된 문장을 리스트에 추가
    - EOS 문장이 충분히 모이면 탐색 종료
    - 각 후도 점수를 로그 확률의 합으로 구해 최종 선택

## Attention

Bottle neck problem이란?
→ 인코더는 입력 문장 전체를 하나의 벡터로 요약하는데, 마지막 hidden state에 문장의 모든 의미 정보가 담긴다. 정보 손실 발생.

Attention이란?
→ 디코더가 단어를 생성할 때, 인코더 전체 hidden state 중 필요한 부분을 직접 참조하도록 함

![image.png](/images/notion-ec7a5661/image%209.png)

## Transformer

## RNN의 한계점

1. 장기 의존성
    
    먼 단어 쌍이 상호작용하려면 시퀀스 길이만큼 단계를 거쳐야 한다.
    
2. 병렬화
    
    Forward와 Bachward pass 모두 시퀀스 길이만큼 단계가 필요해서 병렬화가 불가하다
    

## Self-Attention

![image.png](/images/notion-ec7a5661/image%2010.png)

![image.png](/images/notion-ec7a5661/image%2011.png)
