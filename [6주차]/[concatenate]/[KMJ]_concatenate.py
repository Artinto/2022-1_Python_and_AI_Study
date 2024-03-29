import numpy
n, m, p = map(int, input().split())

array_1 = numpy.array([input().split() for _ in range(n)],int)
array_1.shape = (n, p)

array_2 = numpy.array([input().split() for _ in range(m)],int)
array_2.shape = (m, p)

print(numpy.concatenate((array_1, array_2), axis=0))


# (n+m)*p 형태의 배열로 수정해야 하므로, shape가 필요하다
