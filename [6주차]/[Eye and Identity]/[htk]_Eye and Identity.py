import numpy
numpy.set_printoptions(legacy='1.13')#각 숫자 사이에 폭을 1.13으로 설정
a,b=map(int,input().split())#input을 map 함수를 이용해 input값을 정렬해주고 그를 정수형리스트로 바꿔준다.
print(numpy.eye(a ,b))#eye함수를 이용해 a*b의 단위행렬을 생성
