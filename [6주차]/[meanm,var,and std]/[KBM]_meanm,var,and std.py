import numpy
N,M = list(map(int, input().split()))
a = numpy.array([list(map(int, input().split())) for _ in range(N)])
print(numpy.mean(a, axis=1))
print(numpy.var(a, axis=0))
print(round(numpy.std(a,axis=None),11))
