import numpy

N = int(input())
A = numpy.array([input().split() for _ in range(N)], float)
print(numpy.linalg.det(A))
