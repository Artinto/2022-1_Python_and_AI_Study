import numpy
m,n=input().split(' ')
m=int(m)
g=[]
for i in range(m):
    arr = input().strip().split(' ')
    b=numpy.array(arr,int)
    g.append(b)
print(numpy.transpose(g))
g=numpy.array(g)
print(g.flatten())
