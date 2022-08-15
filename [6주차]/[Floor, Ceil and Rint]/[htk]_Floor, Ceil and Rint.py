import numpy
numpy.set_printoptions(legacy='1.13')#각 숫자 사이에 폭을 1.13으로 설정
a=numpy.array(input().split(),float)#주어진 input값을 정렬한 후에, 실수로 변형시키고 행렬로 나타낸 것을 a라 설정
print(numpy.floor(a))#내림
print(numpy.ceil(a))#올림
print(numpy.rint(a))#반올림
