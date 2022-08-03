M,N = input().split()
M = int (M)
N = int (N)
pattern = [('.|.'*(2*i+1)).center(N,'-')for i in range(M//2)]
print('\n'.join(pattern + ['WELCOME'.center(N,'-')] + pattern[::-1]))
