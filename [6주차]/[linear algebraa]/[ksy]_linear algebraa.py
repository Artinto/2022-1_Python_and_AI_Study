#linear algebraa
import numpy
m = int(input())
arr1 = numpy.array([input().split() for _ in range(m)],float)


print (round(numpy.linalg.det(arr1),2))  
