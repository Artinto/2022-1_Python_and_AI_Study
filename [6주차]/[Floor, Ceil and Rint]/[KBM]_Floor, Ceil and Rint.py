import numpy
numpy.set_printoptions(legacy='1.13') # 공백?
a = numpy.array(input().split(),float)
print(numpy.floor(a))
print(numpy.ceil(a))
print(numpy.rint(a))
