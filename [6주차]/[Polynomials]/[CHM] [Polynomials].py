import numpy
p=input().split()
arr=numpy.array(p,float)
x=int(input())
print(numpy.polyval(arr,x))
