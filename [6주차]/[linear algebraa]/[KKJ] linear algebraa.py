import numpy

n = int(input())
a = numpy.array([input().strip().split() for _ in range(n)], float)
print(float(numpy.linalg.det(a)))
