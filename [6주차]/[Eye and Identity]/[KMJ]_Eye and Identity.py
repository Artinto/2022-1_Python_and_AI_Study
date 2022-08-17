import numpy
numpy.set_printoptions(legacy='1.13')
print (numpy.eye(*map(int,input().split())))

# 숫자 사이의 폭을 지정할 때는 numpy.set_printoptions(legacy='원하는 숫자')를 사용한다
# 해당 예시는 입력값이 둘다 3이므로, print numpy.identity(input())으로 작성해도 된다
