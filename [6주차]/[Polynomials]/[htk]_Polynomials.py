import numpy
a=numpy.array(input().split(),float)#주어진 input 값을 먼저 정렬 한 후에 실수로 변형해준 행렬을 a라 선언
b=int(input())#주어진 input값을 정수로 변형
print(numpy.polyval(a,b))#a의 식에 b의 값을 대입해서 결과값을 반환한다
