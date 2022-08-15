import numpy
n=int(input())
a=numpy.array([input().split() for i in range(n)],float)#주어진 input 값을 먼저 정렬 한 후에,  이런 것을 n번 반복한후 실수로 변형해준것을 행렬 a라 선언한다
print(round(numpy.linalg.det(a),2))#소수 2째자리 까지 a의 행렬식을 계산해 출력

