import numpy

a,b = map(int,input().split())
List=[]
for i in range(a):
 List.append(list(map(int,input().split())))
arr=numpy.array(List)

print(numpy.mean(arr,axis=1))
print(numpy.var(arr,axis=0))
print(round(numpy.std(arr),11))
