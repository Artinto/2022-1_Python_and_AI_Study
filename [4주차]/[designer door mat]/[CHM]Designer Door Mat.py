pattern=[".","|",".","-"]
design="WELCOME"
a, b = map(int, input().split())

for i in range(1,a+1,2):
  A=''.join(pattern[:-1])*(i)
  if i== a:
   print(design.center(b,pattern[-1]))
   continue
  print(A.center(b, pattern[-1]))
for j in range(a-2,0,-2):
  A=''.join(pattern[:-1])*(j)
  print(A.center(b, pattern[-1]))
