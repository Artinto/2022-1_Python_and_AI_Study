from torch import nn, tensor
import numpy as np 
import tensorflow as tf
from keras.datasets import cifar10
import torch.nn.functional as F
# keras 데이터셋에서 cifar10 불러오기



(x_train, y_train), (x_test, y_test) = cifar10.load_data()
# cifar10에서 데이터 가져오기
print('x_train shape:', x_train.shape)
print('y_train shape:', y_train.shape)
print('train sample:', x_train.shape[0])
print('test sample:', x_test.shape[0])
Y = np.squeeze(y_train, axis=1)
# [[6][9][9]...[9][1][1]] 2차원으로 되어있는 데이터를 1차원으로 바꾸는 코드
# y_train = to_categorial(y_train)은 y_train을 원핫으로 바꾸는 코드
print(Y)



class Y_set(nn.Module):
  
    def __init__(self):
        super(Y_set, self).__init__()
        self.l1 = nn.Linear(32*32*3,1000)
        self.l2 = nn.Linear(1000, 500)
        self.l3 = nn.Linear(500, 100)
        self.l4 = nn.Linear(100, 10)


    def forward(self, Y):
        Y = Y.view(-1,32*32*3)
        Y = F.relu(self.l1(Y))
        Y = F.relu(self.l2(Y))  
        Y = F.relu(self.l3(Y))
        Y = F.relu(self.l4(Y))

        return self.l4(Y)



print(Y)
