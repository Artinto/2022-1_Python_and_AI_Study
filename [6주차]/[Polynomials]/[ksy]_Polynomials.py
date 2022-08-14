import numpy

arr= list(map(float,input().split()))
n=int(input())

print(numpy.polyval(arr,n))
