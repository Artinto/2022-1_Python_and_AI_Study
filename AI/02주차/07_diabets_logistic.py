from torch import nn, optim, from_numpy
# torch에서 nn,optim,from_numpy 불러오기
import numpy as np
# numpy를 불러오는데 앞으로 np라고 줄여서 부를 것임

xy = np.loadtxt('./data/diabetes.csv.gz', delimiter=',', dtype=np.float32)
# x와 y에 당뇨병에 관한 자료를 로드
x_data = torch.from_numpy(xy[:, 0:-1])
# numpy 배열을 torch 텐서로 연결하여 초기화(크기를 적당히 잘라서 x_data에 대입)
y_data = torch.from_numpy(xy[:, [-1]])
# numpy 배열을 torch 텐서로 연결하여 초기화
print(f'X\'s shape: {x_data.shape} | Y\'s shape: {y_data.shape}')
# x데이터와 y데이터의 배열 형태 출력


class Model(nn.Module):
#torch.nn.Module을 상속받음
    def __init__(self):
        """
        In the constructor we instantiate two nn.Linear module
        """
        super(Model, self).__init__()
        # super은 부모 클래스를 초기화시켜 부모클래스의 속성을 그 아래 클래스에서 사용할 수 있게 한다.
        # 그러나 여기는 (파생클래스, self)로 되어있으므로 현재의 클래스가 어떤 클래스인지 명시하는 용으로 사용된다.
        self.l1 = nn.Linear(8, 6)
        # 실질적인 연산을 할 선형회귀 모델1 생성
        # x데이터가 (n,8)이므로 8로 시작되어야 함
        self.l2 = nn.Linear(6, 4)
        # 실질적인 연산을 할 선형회귀 모델2 생성
        self.l3 = nn.Linear(4, 1)
        # 실질적인 연산을 할 선형회귀 모델3 생성
        # y데이터가 (n,1)이므로 1로 끝나야함.

        self.sigmoid = nn.Sigmoid()
        # 시그모이드 함수를 self.sigmoid로 지정
        


    def forward(self, x):
    # 예측을 수행하는 함수
        """
        In the forward function we accept a Variable of input data and we must return
        a Variable of output data. We can use Modules defined in the constructor as
        well as arbitrary operators on Variables.
        """
        out1 = self.sigmoid(self.l1(x))
        # x를 self.l1에 넣고 시그모이드함수에 넣은 값을 out1로 지정
        out2 = self.sigmoid(self.l2(out1))
        # out1를 self.l2에 넣고 시그모이드함수에 넣은 값을 out2로 지정
        y_pred = self.sigmoid(self.l3(out2))
        # out2를 self.l3에 넣고 시그모이드함수에 넣은 값을 y_pred로 지정
        # linear layer를 3개로 형성하여 시그모이드 함수를 통과시킴  
        return y_pred
        # y_pred값 반환
      


# our model
model = Model()
# 모델 객체 생성


# Construct our loss function and an Optimizer. The call to model.parameters()
# in the SGD constructor will contain the learnable parameters of the two
# nn.Linear modules which are members of the model.
criterion = nn.BCELoss(reduction='mean')
# gradient를 자동으로 계산해서 최적화를 진행하는 손실함수 구현
# 두개 이상의 클래스는 MCE가 아니라 BCE를 사용
# BCELoss함수(이진분류)를 사용할 경우에는 먼저 마지막 레이어의 값이 0~1로 조정을 해줘야하기 때문에 마지막 레이어에 시그모이드함수 사용하여야 함
optimizer = optim.SGD(model.parameters(), lr=0.1)
# 최적화 부분 구현, leaning rate는 0.1


# Training loop
for epoch in range(100):
  # epoch를 100번 
    # Forward pass: Compute predicted y by passing x to the model
    y_pred = model(x_data)
    # 모든 x데이터를 행렬형태로 모델에게 넘겨주기
    

    # Compute and print loss
    loss = criterion(y_pred, y_data)
    # criterion이라는 함수를 이용하여 예측과 정답을 비교하는 평가 진행
    print(f'Epoch: {epoch + 1}/100 | Loss: {loss.item():.4f}')
    # epoch와 loss 출력

    # Zero gradients, perform a backward pass, and update the weights.
    optimizer.zero_grad()
    # gradent descent 직전에 초기화
    loss.backward()
    # 구한 loss로부터 한칸 뒤로 가 gradient를 구하기
    optimizer.step()
    # step()을 이용하여 지정해 준 model의 파라미터 값 업데이트
