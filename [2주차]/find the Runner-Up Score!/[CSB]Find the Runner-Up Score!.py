if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    A=list(set(arr))
    A.reverse()
    print(A[1])
