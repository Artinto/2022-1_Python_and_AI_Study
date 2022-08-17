import numpy

arr = numpy.array(input().split(), int)
print(numpy.zeros(arr, int))
print(numpy.ones(arr, int))

# 입력값이 몇 개인지 정해지지 않았으므로 array형태로 값을 받아온다.
numpy.zeros는 0을, numpy.ones는 1을 출력한다.
