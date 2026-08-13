---
title: "AI자습 1 (Tensor, nn.Module, Dataset)"
publishedAt: 2026-08-10
---
<!-- notion-import-source: notion-export-e775a72346d248c6b445f60770f9e280 -->

## Tensor (PyTorch)

```python
import torch

torch.tensor([1.0, 2.0, 3.0])
matrix = torch.zeros(3, 4)
random_tensor = torch.randn(2, 3)
```

## Numpy와 변환

```python
import numpy as np

np_aray = np.array([1, 2, 3])
tensor = torch.from_numpy(np_array)
np_back = tensor.numpy()
```

## Tensor 속성

```python
print(tensor.shape, tensor.dtype, tensor.device)
```

## Autograd (자동 미분)

```python
x = torch.tensor([2.0, 3.0], requires_grad = True)
y = x ** 2 + 3 * x
z = y.sum()
z.backward()

print(f"x.grad = {x.grad}")
```

x를 ‘미분 예정’인 텐서로 생성
x에 대한 이차식 y 작성 → y = [10.0, 18.0]
y의 원소를 모두 더해 스칼라값으로 변경 → z = 28.0
이후 역전파 진행 → x에 미분값이 저장됨

## nn.Module

```python
import torch
import torch.nn as nn

class MyModel(nn.Module):

	def __init__(self):
		super().__init__()
		
		self.layer1 = nn.Linear(784, 256)
		self.relu = nn.ReLU()
		self.layer2 = nn.Linear(256, 10)
		
	def forward(self, x):
		x = self.relu(self.layer1(x))
		x = self.layer2(x)
		
		return x
```

## nn.Sequential

```python
model = nn.Sequential(
	nn.Linear(784, 256),
	nn.ReLU(),
	nn.Dropout(0.2),
	nn.Linear(256, 128),
	nn.ReLU(),
	nn.Linear(128, 10)
	)
```

![image.png](/images/notion-e775a723/image.png)

## Dataset

한번에 학습 데이터를 메모리에 다 올리면 OOM에러로 터져버린다.
그래서 Dataset이라는 방법을 쓴다

## TensorDataset

텐서를 직접 감싸는 가장 간단한 Dataset

```python
import torch
from torch.util.data import TensorDataset

X_tensor = torch.FloatTensor([[1, 2], [3, 4], [5, 6], [8, 8]])
y_tensor = torch.LongTensor([0, 1, 0, 1])

dataset = TensorDataset(X_tensor, y_tensor)

print(f"데이터 수: {len(dataset)}")
print(f"첫 번째 샘플: {dataset[0]}")
```

## 커스텀 데이터셋

__len__과 __getitem__을 구현하여 자유로운 데이터 로딩이 가능함

```python
from torch.utils.data import Dataset

class MyDataset(Dataset):
	def __init__(self, X, y):
		self.X = torch.FloatTensor(X)
		self.y = torch.LongTensor(y)
		
	def __len__(self):
		return len(self.X)
		
	def __getitem__(self, idx):
		return self.X[idx], self.y[idx]
```

## DataLoader

Data를 배치 단위로 순회할 수 있게 하는 Iterator

```python
from torch.utils.data import DataLoader

loader = DataLoader(dataset, batch_size = 2, shuffle = True)

for batch_idx, (batch_X, batch_y) in enumerate(loader):
	print(f"Batch {batch_idx}: X shape = {batch_X.shape}, y = {batch_y.tolist()}")
```

- enumerator란?
    
    → (인덱스 번호, 데이터) 형태의 튜플로 묶어서 반환해줌. 데이터 인덱스 필요할때 for문에서 자주 사용
    

### 학습 루프에서 사용

```python
import torch.nn as nn
import torch.optim as optim

model = nn.Linear(2, 2)
cross-entropy = nn.CrossEntropyLoss()
optimizer = optim.SGD(model.parameters(), lr = 0.01)
num_epochs = 5
 
for epoch in num_epochs:
	for batch_X, batch_y, in loader:
		output = model(batch_X)
		loss = cross_entropy(output, batch_y)
		
		optimizer.zero_grad()
		loss.backward()
		optimizer.step()
		
		 print(f"Epoch {epoch+1}/{num_epochs}, Loss: {loss.item():.4f}")
```
