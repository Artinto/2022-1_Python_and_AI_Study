import numpy

def arrays(arr): 
    arr.reverse()
    a = numpy.array(arr, float)
    return a

arr = input().strip().split(' ') 
result = arrays(arr)
print(result)
