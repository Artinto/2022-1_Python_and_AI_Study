N,M = input().split()
pattern ='.|.'

N = int(N)
M = int(M)
a = N//2-1 

for i in range(N):
    if i == N//2:
        print('WELCOME'.center(M,'-'))
    elif i < N/2:    
        print((pattern*(2*i+1)).center(M,'-'))
    else: 
        print((pattern*(2*a+1)).center(M,'-'))
        a = a-1
