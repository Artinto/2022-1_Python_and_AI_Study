#Arrays
import numpy

def arrays(arr):
   
    a=numpy.array(arr,float)
    a=numpy.flip(a)
    return a

arr = input().strip().split(' ')
result = arrays(arr)
print(result)
