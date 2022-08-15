import numpy
n , m= map(int, input().split())# n,m을 map함수를 이용해 input값을 정렬해주고 그를 정수형리스트로 바꿔준다.
a=numpy.array([input().split() for i in range(n)],int)#주어진 input 값을 먼저 정렬 한 후에,  이런 것을 n번 반복한후 정수로 변형해준것을 행렬 a라 선언한다
print (numpy.prod(numpy.sum(a,axis=0)))#그 후에 a의 원소들을 수직방향으로 합치기 위해 axis=으로 설정후 각 부분을 더한 후에 그 더한 원소를 곱으로 사용
