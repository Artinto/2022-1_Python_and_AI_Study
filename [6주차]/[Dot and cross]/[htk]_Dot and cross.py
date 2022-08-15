import numpy
n=int(input())
a=numpy.array([input().split() for i in range(n)],int)#주어진 input 값을 먼저 정렬 한 후에,  이런 것을 n번 반복한후 정수로 변형해준것을 행렬 a라 선언한다
b=numpy.array([input().split() for i in range(n)],int))#주어진 input 값을 먼저 정렬 한 후에,  이런 것을 n번 반복한후 정수로 변형해준것을 행렬 a,b라 선언한다. 
print (numpy.dot(a, b))# 그 후에 내적을 a와 b의 내적 실행
