x = int(input())
y = int(input())
z = int(input())
n = int(input())
b=[]
for i in range(x+1):
  for j in range(y+1):
    for k in range(z+1):
      a=[]
      a.append(i)
      a.append(j)
      a.append(k)
      if i+j+k !=n:
         b.append(a)
     
print(b)


