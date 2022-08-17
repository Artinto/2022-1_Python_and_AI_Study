import numpy

a,b = map(int,input().split())
List=[]
for i in range(a):
 List.append(list(map(int,input().split())))
arr=numpy.array(List)
Min=numpy.min(arr,axis=1)
print(numpy.max(Min,axis=0))
