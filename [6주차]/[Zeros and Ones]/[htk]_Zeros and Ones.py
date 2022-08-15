5.
import numpy
n,m,*o=map(int,input().split())#n과 m은 map 함수를 이용해 input값을 정렬해주고 그를 정수형리스트로 바꿔준다. 이때 *o는 *o를 사용하지 않거나 여러개를 사용한다고 말하는 것이다.
a= numpy.zeros((n,m,*o),dtype=numpy.int)#n.m.*o의 0으로만 구성된 정수형 행렬 설정
b= numpy.ones((n,m,*o),dtype=numpy.int)#n.m.*o의 1로만 구성된 정수형 행렬 설정
print(a)
print(b)
