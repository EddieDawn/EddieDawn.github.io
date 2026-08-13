---
title: "AI자습 1 (단계별 MLP 구현)"
publishedAt: 2026-08-10
---
<!-- notion-import-source: notion-export-751cb4bff5194cb2bd5eddd720cd6fb1 -->

## MLP (Multi - Layer Perceptron)

여러 Fully Connected Layer를 쌓아 비선형 문제를 해결하는 신경망

nn.Linear를 아무리 쌓아도, 중첩된 선형 변환은 그냥 선형 변환일 뿐. 결국 단층 선형 모델이다.
그래서 각 레이어 사이 비선형 함수를 넣어서 등가 축약을 막는거임

## 차근차근 구현해봅시다

## Dataset로드, feature과 target 분리

```python
from sklearn.datasets import load_digits

digits_dataset = load_digits()
features = digits_dataset.data
target = digits_datset.target
```

load_digits()해서 받아온 digits_dataset은 Bunch라는 특이한 파이썬 객체임. 약간 Dictionary랑 비슷함
그래서 .data, .target같은 dot을 찍어서 접근이 가능함

## 학습 / 테스트 데이터 분할

```python
from sklearn.model_selection import train_test_split

features_train, features_test, target_train, target_test = train_test_split(
	features, target, test_size=0.2, random_state=42, stratify=target
)
```

strafity는 test, train데이터셋에서 label분포를 동일한 비율로 가져가겠다는거임

## 표준화

```python
from sklearn.preprocessing import StandardScaler

standard_scaler = StandardScaler()
feature_train_scaled = standard_scaler.fit_transform(features_train)
feature_test_scaled = standard_scaler.transform(features_test)

print(f"{feature_train_scaled[:,4].mean():.2f},}")
```

## NP를 Tensor로 바꾸자

```python
features_train_tensor = torch.from_numpy(feature_train_scaled).float()
features_test_tensor = torch.from_numpy(feature_test_scaled).float()
target_train_tensor = torch.from_numpy(target_train).float()
target_test_tensor = torch.from_numpy(target_test).float()
```

왜 바꿈? DataLoader랑 nn.Module은 ndarray가 아닌 tensor를 자료형으로 받으니까

## Datast 만들기

```python
from torch.utils.data import TensorDataset, DataLoader

train_dataset = TensorDataset(features_train_tensor, target_train_tensor)
test_dataset = TensorDataset(features_test_tensor, target_test_tensor)
BATCH_SIZE = 32

train_loader = DataLoader(train_dataset, batch_size = BATCH_SIZE, shuffle = True)
validate_loader = DataLoader(test_dataset, batch_size = BATCH_SIZE, shuffle = False)
```

## MLP 클래스 구조 만들기

```python
class MLP(nn.Module):
	
	def __init__:(self, input_dim, num_classes, hidden_dims(128, 46), dropout=0.2):
		super().__init__
		
		layers = []
		pervious_dim = input_dim
		
		for hidden_dim in inffen_dims:
			layers.append(nn.Linear(pervious_dim, hidden_dim))
			layers.append(nn.ReLU())
			layers.append(nn.Dropdout(dropout))
			pervious_dim = hidden_dim
			
		layers.append(nn.Linear(previous_dim, num_classes))
		
		self.network = nn.Sequential(*layers)
		
		def forward(self, input_tensor):
			return self.network(input_tensor)
```

이렇게 MLP 구조를 클래스에 저장해 놓고

```python
mlp_model = MLP(input_dim = 64, num_classes = 10)
```

이렇게 객체 만들어서 쓰기

## 손실 함수와 옵티마이저

```python
cross_entropy = nn.CrossEntropy()
optimizer = optim.Adam(mlp_model.parameters(), lr=1e-3, weight_decay=1e-4)
```

Adam: Adaptive Moment Estimation 뭘쓸지 모르겠으면 아담을 써라.

```python
epochs=50
train_loss_list = []
train_accuracy_list = []
validation_loss_list = []
validation_accuracy_list = []
```

## Train loop

```python
for epoch in epochs:
	
	# 학습 모드로 전환
	mlp_model.train() 
	total_loss, correct, total = 0, 0, 0
	
	for features_batch, target_batch in train_loader:
		optimizer.zero_grad()
		output = mlp_model(features_batch)
		loss = cross_entropy(output, target_batch.long())
		
		loss.bachward()
		optimizer.step()
		
		total loss += loss.item() * len(target_batch)
		correct += (output.argmax(1) == target_batch).sum().item()
    total += len(target_batch)
    
  train_loss = total_loss / total
  train_accuracy = correct / total
  train_loss_list.append(train_loss)
  train_accuracy_list.append(train_accuracy)
  
  #평가 모드로 전환
  mlp_model.eval()
  validation_correct, validation_total, validation_loss_sum = 0, 0, 0
  
 with torch.no_grad():
    for features_batch, target_batch in validation_loader:
      output = mlp_model(features_batch)
      loss = cross_entropy(output, target_batch.long())
      validation_loss_sum += loss.item() * len(target_batch)
      validation_correct += (output.argmax(1) == target_batch).sum().item()
      validation_total += len(target_batch)
	        
	validation_loss = validation_loss_sum / validation_total
	validation_accuracy = validation_correct / validation_total
	validation_loss_list.append(validation_loss)
	validation_accuracy_list.append(validation_accuracy)
	
	if (epoch + 1) % 10 == 0:
      print(f"Epoch {epoch+1:2d}: Loss={train_loss:.4f}, "
          f"Train Acc={train_accuracy:.2%}, Val Acc={validation_accuracy:.2%}")  
```

## Early Stopping, Checkpoint

```python
# TODO 13: 저장된 가중치를 불러와 모델에 적용하고, 평가 모드로 전환해봅시다.
loaded_model = MLP(input_dim=64, num_classes=10)
loaded_model.load_state_dict(torch.load("best_model.pt", weights_only=True))
loaded_model.eval()
print("모델 로드 완료")
```

```python
best_validation_loss = float("inf")
patience = 5
patience_counter = 0  # 1. 성능이 안 오르는 연속 횟수를 세는 카운터 추가

for epoch in range(epochs):
    
    # ... [학습(Train) 및 검증(Validation) 진행 코드 생략] ...

    # 2. 검증 손실 비교 및 조기 종료 판단
    if validation_loss < best_validation_loss:
        best_validation_loss = validation_loss
        torch.save(mlp_model.state_dict(), "best_model.pt")
        print(f"  ✓ Best model saved (validation_loss={validation_loss:.4f})")
        
        # 성능이 개선되었으므로 카운터를 다시 0으로 리셋합니다.
        patience_counter = 0
    else:
        # 이전 최고 기록보다 손실이 낮아지지 않았다면 카운터를 1 증가시킵니다.
        patience_counter += 1
        print(f"  ! No improvement in validation loss ({patience_counter}/{patience})")
        
        # 연속으로 5번(patience) 동안 개선이 없으면 학습을 즉시 중단합니다.
        if patience_counter >= patience:
            print(f"\n Early stopping triggered at epoch {epoch + 1}!")
            break  # 가장 바깥쪽의 for epoch 루프를 강제로 탈출합니다.
```

최고 성능 모델을 백업해놓는 식. 모델 성능 개선이 없으면 patience횟수만큼 기다려줌.

## GPU 활용

```python
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"사용 장치: {device}")

mlp_model = mlp_model.to(device)

# 배치 데이터도 같은 장치로 이동
sample_features, sample_target = next(iter(train_loader))
sample_features = sample_features.to(device)
sample_target = sample_target.to(device)
```
