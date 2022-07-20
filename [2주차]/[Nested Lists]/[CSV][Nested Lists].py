if __name__ == '__main__':
    A=[0]
    D=[0]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        A.append(score)
        D.append(name)
C=list(set(A))
C.sort()
if C[1]<0:
    C.reverse()

B=[]

for i in range(0,len(A)):
  if A[i]==C[2]:
    B.append(D[i])
B.sort()
for j in range(0, len(B)):
    print(B[j])
