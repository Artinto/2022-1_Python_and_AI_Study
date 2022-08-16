import numpy
n, m = map(int, input().split())
storage = numpy.array([input().strip().split() for _ in range(n)], int)
print (storage.transpose()) #전치행렬
print (storage.flatten()) #평탄화
