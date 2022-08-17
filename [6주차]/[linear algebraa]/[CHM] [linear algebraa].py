n=int(input())
List=[]
for i in range(n):
 List.append(list(map(float,input().split())))
arr=numpy.array(List)
print(round(numpy.linalg.det(arr),2))
