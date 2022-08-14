import numpy
N, M = map(int, input().split())
a = numpy.array([input().strip().split() for _ in range(N)], int) 
print (a.transpose())
print (a.flatten())
