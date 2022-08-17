import numpy
Y = numpy.array(input().split(), float)
x = float(input())

print(numpy.polyval(Y, x)) #polyval : 다항식의 계수로부터 값 계산
