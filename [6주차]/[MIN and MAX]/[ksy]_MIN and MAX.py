import numpy as np
m,n = map(int,input().split())
arr1 = np.array([input().split() for _ in range(m)],int)


arr1=np.min(arr1, axis = 1)
print (np.max(arr1))
