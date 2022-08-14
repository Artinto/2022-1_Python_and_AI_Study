import numpy as np
a, b, c = map(int,input().split())  #int 화 시키기 편하게 map사용  여기서 c의 활용도는??
arr1 = np.array([input().split() for _ in range(a)],int)
arr2 = np.array([input().split() for _ in range(b)],int)
print(np.concatenate((arr1, arr2), axis = 0))##axis 차원수?
