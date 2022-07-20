x=int(input())
y=int(input())
z=int(input())
n=int(input())

c=[]
for i in range(x+1):
  for j in range(y+1):
    for k in range(z+1):
      b=[i,j,k]
      if i+j+k != n:
       c.append(b)
print(c)
