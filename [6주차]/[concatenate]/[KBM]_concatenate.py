import numpy
N, M, P = map(int, input().split())
a = numpy.array([input().strip().split() for _ in range(N)], int) 
b = numpy.array([input().strip().split() for _ in range(M)], int) 
print (numpy.concatenate((a, b), axis=0))    
