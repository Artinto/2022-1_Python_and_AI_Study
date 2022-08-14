import numpy as np
m,n = map(int,input().split())
arr1 = np.array([input().split() for _ in range(m)],int)

arr1=np.sum(arr1, axis = 0) 
print (np.prod(arr1)) 
