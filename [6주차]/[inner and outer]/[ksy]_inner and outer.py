import numpy as np

arr1 = np.array(input().split(),int)
arr2 = np.array(input().split(),int)

print(np.inner(arr1,arr2))
print(np.outer(arr1,arr2))
