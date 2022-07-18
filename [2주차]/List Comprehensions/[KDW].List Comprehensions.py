if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    result=[]
    
    x1=list(range(0,x+1))
    y1=list(range(0,y+1))
    z1=list(range(0,z+1))
    
    for i in x1:
        for j in y1:
            for k in z1:
                if i+j+k==n:
                    continue
                
            
                result.append([i,j,k])
    print(result)
                
                
