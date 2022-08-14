import numpy as np
m,n = map(int,input().split())
arr1 = np.array([input().split() for _ in range(m)],float)
print (np.mean(arr1, axis = 1))
print (np.var(arr1, axis = 0) )
print(round(np.std(arr1),11))
