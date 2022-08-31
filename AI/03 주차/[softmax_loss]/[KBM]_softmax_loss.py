# import
from torch import nn, tensor, max    # torch에서 라이브러리 nn, tensor, max 임포트  
import numpy as np # numpy 라이브러리를 nn 으로 임포트

# (1) Cross entropy example
Y = np.array([1, 0, 0])  # Y : 실제값 (0 or 1)
Y_pred1 = np.array([0.7, 0.2, 0.1])  # Y_pred1 : 에측의 확률 값 ( 0 ~ 1 )
Y_pred2 = np.array([0.1, 0.3, 0.6])  # Y_pred2 : 예측의 확률 값 ( 0 ~ 1 )
print(f'Loss1: {np.sum(-Y * np.log(Y_pred1)):.4f}')  # Loss1: 0.3567
print(f'Loss2: {np.sum(-Y * np.log(Y_pred2)):.4f}')  # Loss2: 2.3026 

# (1)
# Loss1 = - {0*log(0.1) + 0*log(0.2) + 1*log(0.7)} = -log(0.7) = 0.3567
# Y_pred1 이  Y_pred2 보다 잘한 예측. (Loss 값 Y_pred2 가 더 큼.)
# One hot : 원-핫 인코딩은 선택해야 하는 선택지의 개수만큼의 차원을 가짐/
# 각 선택지의 인덱스에 해당하는 원소 1, 나머지 원소는 0의 값으로 표현
# ex) 0: 1 0 0 / 1: 0 1 0 / 2: 0 0 1

# (2) Softmax + CrossEntropy (logSoftmax + NLLLoss)
loss = nn.CrossEntropyLoss()
# 파이토치에서 softmax가 포함된 cross-entropy함수 제공. (Loss 함수를 적용하기 위해 softmax 우선 사용 X.)

# target is of size nBatch
# each element in target has to have 0 <= value < nClasses (0-2)
# Input is class, not one-hot
Y = tensor([0], requires_grad=False)  # 실제값 Y : 인덱스(클래스)[0]

# input is of size nBatch x nClasses = 1 x 4
# Y_pred are logits (not softmax)
Y_pred1 = tensor([[2.0, 1.0, 0.1]])  # 맞는 예측 (인덱스0의 logit값이 가장 큼)
Y_pred2 = tensor([[0.5, 2.0, 0.3]])  # 틀린 예측, 손실값 큼
# logit 값 그대로 손실 함수에 입력

l1 = loss(Y_pred1, Y)  # loss(예측값, 실제값)
l2 = loss(Y_pred2, Y)  #  예측값은 logit값(확률 값X), Y는 원핫벡터가 아닌 class 이름(0,1,2).

print(f'PyTorch Loss1: {l1.item():.4f} \nPyTorch Loss2: {l2.item():.4f}') #PyTorch Loss1: 0.4170 ,PyTorch Loss2: 1.8406   
# 예상과 같이 Y_pred2의 틀린예측을 한 손실값이 큰 것 확인.
print(f'Y_pred1: {max(Y_pred1.data, 1)[1].item()}') # 1과 data중 큰값의 인덱스만 출력
print(f'Y_pred2: {max(Y_pred2.data, 1)[1].item()}')

# (3) mulitple
# target is of size nBatch
# each element in target has to have 0 <= value < nClasses (0-2)
# Input is class, not one-hot
Y = tensor([2, 0, 1], requires_grad=False) # Y : 실제값 (각 행에서 가장 큰 logit값의 클래스)/ 원핫벡터X 

# input is of size nBatch x nClasses = 2 x 4
# Y_pred are logits (not softmax)
Y_pred1 = tensor([[0.1, 0.2, 0.9],
                  [1.1, 0.1, 0.2],
                  [0.2, 2.1, 0.1]])  # 잘한 예측

Y_pred2 = tensor([[0.8, 0.2, 0.3],
                  [0.2, 0.3, 0.5],
                  [0.2, 0.2, 0.5]])  # 틀린 예측

l1 = loss(Y_pred1, Y)  # Batch Loss1:  0.4966 
l2 = loss(Y_pred2, Y)  # Batch Loss2: 1.2389
print(f'Batch Loss1:  {l1.item():.4f} \nBatch Loss2: {l2.data:.4f}')
