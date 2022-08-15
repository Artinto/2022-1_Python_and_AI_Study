import numpy
a=numpy.array([input().split()],int)#주어진 input 값을 먼저 정렬 한 후에 정수로 변형해준 행렬을 a라 선언
b=numpy.array([input().split()],int)#주어진 input 값을 먼저 정렬 한 후에 정수로 변형해준 행렬을 b라 선언
print (numpy.inner(a, b))#내적
print (numpy.outer(a, b))#외적
