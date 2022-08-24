# References
# https://github.com/yunjey/pytorch-tutorial/blob/master/tutorials/01-basics/pytorch_basics/main.py
# http://pytorch.org/tutorials/beginner/data_loading_tutorial.html#dataset-class
from torch.utils.data import Dataset, DataLoader
# torch.utils.data에서 Dataset, DataLoader 라이브러리 가져오기
from torch import from_numpy, tensor
# torch에서 from_numpy, tensor 라이브러리 가져오기
import numpy as np
# numpy 라이브러리 가져오는데 np라고 부를 것임

class DiabetesDataset(Dataset):
    """ Diabetes dataset."""
    # DiabetesDataset(Dataset)은 사용자가 DataSet을 custom하는 부분(배치를 만드는 부분)
    # DataSet 클래스를 확장하는 별도의 클래스 DiabetesDataset

    def __init__(self):
    # dataset 전처리하는 부분
        xy = np.loadtxt('./data/diabetes.csv.gz',
                        delimiter=',', dtype=np.float32)
        # x와 y에 당뇨병에 관한 자료를 로드
        self.len = xy.shape[0]
        # x와 y의 길이 계산
        self.x_data = torch.from_numpy(xy[:, 0:-1])
        # numpy 배열을 torch 텐서로 연결하여 초기화
        self.y_data = torch.from_numpy(xy[:, [-1]])
        # numpy 배열을 torch 텐서로 연결하여 초기화

    def __getitem__(self, index):
    # 원하는 위치의 index 자료를 가져오기 위해 indexing하는 부분
        return self.x_data[index], self.y_data[index]    
        # 주어진 인덱스에 있는 항목을 x데이터와 y데이터로 변환 

    def __len__(self):
    # dataset의 길이를 가져오는 부분
    	  return self.len
	      # dataset의 길이 반환


dataset = DiabetesDataset()
# 클래스를 호출
train_loader = DataLoader(dataset=dataset,
                          batch_size=32,
                          shuffle=True,
                          num_workers=2)
# 데이터로더에 공급하여 모델의 크기와 셔플여부, 작업자 수 지정
# 32개의 데이터가 한 개의 batch이고, data가 셔플되며, 작업자(cpu)가 2개라는 것을 의미

for epoch in range(2):
# 최적화 2번 반복
    for i, data in enumerate(train_loader, 0):
    # i는 반복횟수, data는 최적화 과정에서 입력되는 data.
        inputs, labels = data
        # 데이터 값 입력

        inputs, labels = tensor(inputs), tensor(labels)
        # 입력값, labels를 텐서 형태로 변형

        print(f'Epoch: {i} | Inputs {inputs.data} | Labels {labels.data}')
        # 최적한 수와 입력 데이터, label 데이터 출력
