import numpy

a=int(input())
num_A=[input().split() for _ in range(a)]
num_B=[input().split() for _ in range(a)]
A=numpy.array(num_A, int)
B=numpy.array(num_B, int)
print(A.dot(B))
