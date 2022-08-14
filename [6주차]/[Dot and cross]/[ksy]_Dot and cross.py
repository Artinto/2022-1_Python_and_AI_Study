import numpy as np
m = int(input())
arr1 = np.array([input().split() for _ in range(m)],int)
arr2 = np.array([input().split() for _ in range(m)],int)

print(np.dot(arr1,arr2))
