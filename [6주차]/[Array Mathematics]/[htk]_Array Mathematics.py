import numpy
n , m= map(int, input().split())# n,m을 map함수를 이용해 input값을 정렬해주고 그를 정수형리스트로 바꿔준다.
a=numpy.array([input().split() for i in range(n)],int)
b=numpy.array([input().split() for i in range(n)],int)#주어진 input 값을 먼저 정렬 한 후에,  이런 것을 n번 반복한후 정수로 변형해준것을 행렬 a,b라 선언한다. 이때 m은 공백이기에 사용하지 않았다.

print(a+b)#더하기
print(a-b)#빼기
print(a*b)#곱하기
print(a//b)#정수구하기
print(a%b)#나머지 구하기
print(a**b)#a의 b 제곱
