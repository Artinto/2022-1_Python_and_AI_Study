if __name__ == '__main__':
    N = int(input())
    b= []
    for a in range(N):
        arr=input().split()
        if arr[0] =="insert":
            b.insert(int(arr[1]),int(arr[2]))
        elif arr[0]=="append":
            b.append(int(arr[1]))
        elif arr[0]=="remove":
            b.remove(int(arr[1]))
        elif arr[0]=="sort":
            b.sort()
        elif arr[0]=="pop":
            b.pop()
        elif arr[0]=="reverse":
            b.reverse()
        elif arr[0]=="print":
            print(b)
