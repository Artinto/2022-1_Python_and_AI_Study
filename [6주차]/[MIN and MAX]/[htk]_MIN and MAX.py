import numpy
n , m= map(int, input().split())# n,m을 map함수를 이용해 input값을 정렬해주고 그를 정수형리스트로 바꿔준다.
a=numpy.array([input().split() for i in range(n)],int)#주어진 input 값을 먼저 정렬 한 후에,  이런 것을 n번 반복한후 정수로 변형해준것을 행렬 a라 선언한다

print(numpy.max((numpy.min(a, axis = 1))))#행렬 a에서 각 행별로 최소값을 구한 다음에 나온 최소값에서 전체의 최대값을 구한다
