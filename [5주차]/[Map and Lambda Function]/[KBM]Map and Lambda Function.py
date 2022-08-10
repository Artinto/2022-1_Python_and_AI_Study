cube = lambda x: pow(x,3)

def fibonacci(n):
    A = [0,1]
    for i in range(2,n):
        A.append(A[i-2] + A[i-1])
    return(A[0:n])
        
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
