import numpy
a,b,c= map(int,input().split())

matrix = []
for i in range(a+b):
  matrix.append(list(map(int, input().split())))
arr=numpy.array(matrix)
print(arr)
