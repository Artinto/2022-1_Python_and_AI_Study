if __name__ == '__main__':
    l=[]
    N = int(input())
    for i in range(N):
        name, *num= input().split()
        a=list(map(str,num))
        if name=='print': 
            print(l)
        elif name=='insert' :
            l.insert(int(a[0]),int(a[1]))
        elif name=='remove':
            l.remove(int(a[0]))
        elif name=='append':
            l.append(int(a[0]))
        elif name=='sort':
            l.sort()
        elif name=='pop':
            l.pop()
        elif name=='reverse':
            l.reverse()
            
