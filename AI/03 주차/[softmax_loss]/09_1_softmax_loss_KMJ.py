from torch import nn, tensor, max
# torch에서 nn, tensor, max 라이브러리를 불러오기
import numpy as np
# numpy 라이브러리를 np라는 이름으로 불러오기

# Cross entropy example
# One hot
# 0: 1 0 0
# 1: 0 1 0
# 2: 0 0 1
# One hot이라는 것은 1개만 1이고 나머지는 0인 value를 의미한다.
Y = np.array([1, 0, 0])
# Y는 정답을 의미 (3개의 class 중 0번이 정답이고 1, 2번은 오답)
Y _pred1 = np.array([0.7, 0.2, 0.1])
# softmax를 사용한 예측값1을 의미 -> 잘된 예측 : 0번째의 확률이 매우 높기 때문
Y_pred2 = np.array([0.1, 0.3, 0.6])
# softmax를 사용한 예측값2를 의미 -> 잘못된 예측 : 0번째의 확률이 낮고 3번째의 확률이 높기 때문
print(f'Loss1: {np.sum(-Y * np.log(Y_pred1)):.4f}')
# CrossEntropy함수를 사용하여 loss출력 -> D(Y_pred,Y) = -YlogY_pred
# 0.35의 값이 나옴
print(f'Loss2: {np.sum(-Y * np.log(Y_pred2)):.4f}')
# CrossEntropy함수를 사용하여 loss출력(원래의 Lable값과 Softmax를 이용하여 구한 확률값과의 loss를 추출 : CrossEntropy)
# 2.3의 값이 나옴

# Softmax + CrossEntropy (logSoftmax + NLLLoss)
loss = nn.CrossEntropyLoss()
#crossentropy 함수를 사용하여 loss를 구함

# target is of size nBatch
# each element in target has to have 0 <= value < nClasses (0-2)
# Input is class, not one-hot
Y = tensor([0], requires_grad=False)
# 여기서 Y는 Onehot이 아니라 정답이 들어있는 class

# input is of size nBatch x nClasses = 1 x 4
# Y_pred are logits (not softmax)
Y_pred1 = tensor([[2.0, 1.0, 0.1]])
# 여기 예측값도 softmax가 아닌 logit이 들어가있음.
# logit은 각각의 class가 정답일 확률 (모든 class의 합이 1이 아님)
# softmax는 모든 class에 대해 해당 class가 정답일 확률 (모든 class의 합이 1)
Y_pred2 = tensor([[0.5, 2.0, 0.3]])

l1 = loss(Y_pred1, Y)
# loss함수를 이용하여 예측값1과 Y의 loss 구하기
l2 = loss(Y_pred2, Y)
# loss함수를 이용하여 예측값2와 Y의 loss 구하기

print(f'PyTorch Loss1: {l1.item():.4f} \nPyTorch Loss2: {l2.item():.4f}')
# loss1과 loss2 print : loss1은 0.41, loss2는 1.84로 1의 loss가 더 작음
# 정답은 0이고 y_pred1은 0번의 확률이 높았고, y_pred는 1번의 확률이 높았기 때문
print(f'Y_pred1: {max(Y_pred1.data, 1)[1].item()}')
# Y_pred가 1보다 크면 배열의 2번째 값 반환, 1보다 작으면 1 반환
### 어떤 의미인지 잘 모르겠습니다
print(f'Y_pred2: {max(Y_pred2.data, 1)[1].item()}')

# target is of size nBatch
# each element in target has to have 0 <= value < nClasses (0-2)
# Input is class, not one-hot
Y = tensor([2, 0, 1], requires_grad=False)
# 다중분류 정답. 첫번째는 2가 정답 두번째는 0이 정답 세번째는 1이 정답인 Y

# input is of size nBatch x nClasses = 2 x 4
# Y_pred are logits (not softmax)
Y_pred1 = tensor([[0.1, 0.2, 0.9],
                  [1.1, 0.1, 0.2],
                  [0.2, 2.1, 0.1]])
# 잘된 예측값
# 첫번째 0.1, 0.2, 0.9에서 0.9가 가장 크므로 2가 정답
# 두번째 1.1, 0.1, 0.2에서 1.1가 가장 크므로 0이 정답
# 세번째 0.2, 2.1, 0.1에서 2.1이 가장 크므로 1이 정답
Y_pred2 = tensor([[0.8, 0.2, 0.3],
                  [0.2, 0.3, 0.5],
                  [0.2, 0.2, 0.5]])
# 잘못된 예측값
# 첫번째 0.8, 0.2, 0.3에서 0.8이 가장 크므로 0이 정답 -> 실제로는 2가 정답
# 두번째 0.2, 0.3, 0.5에서 0.5가 가장 크므로 2가 정답 -> 실제로는 0이 정답
# 세번째 0.2, 0.2, 0.5에서 0.5가 가장 크므로 2가 정답 -> 실제로는 1이 정답


l1 = loss(Y_pred1, Y)
# loss함수를 이용하여 예측값1과 Y의 loss 구하기
l2 = loss(Y_pred2, Y)
# loss함수를 이용하여 예측값2와 Y의 loss 구하기
print(f'Batch Loss1:  {l1.item():.4f} \nBatch Loss2: {l2.data:.4f}')
# loss1과 loss2 print : loss1은 0.5, loss2는 1.24로 1의 loss가 더 작음
