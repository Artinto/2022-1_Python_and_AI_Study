import numpy
numpy.set_printoptions(sign=' ')

array = numpy.array(input().split(),float)

print(numpy.floor(array)) #소수점 아래 내림
print(numpy.ceil(array)) #소수점 아래 올림
print(numpy.rint(array)) #소수점 아래 반올림
