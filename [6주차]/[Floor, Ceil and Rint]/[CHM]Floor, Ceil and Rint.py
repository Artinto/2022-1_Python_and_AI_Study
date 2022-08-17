import numpy
numpy.set_printoptions(legacy='1.13')

a=list(input().split())
arr=numpy.array(a, float)

print(numpy.floor(arr))
print(numpy.ceil(arr))
print(numpy.rint(arr))
