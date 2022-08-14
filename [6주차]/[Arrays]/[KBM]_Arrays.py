import numpy as np

def arryas(arr) : 
    arr.reverse()
    return(np.array(arr, float))

arr = input().strip().split(' ')
result = arryas(arr)
print(result)
