if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    output=[]
    for a in range(0,x+1):
        for b in range(0,y+1):
            for c in range(0,z+1):
                output = [[a,b,c]]
                if a+b+c!=n:
                    output.append([a,b,c])
                    print(output)
                    
