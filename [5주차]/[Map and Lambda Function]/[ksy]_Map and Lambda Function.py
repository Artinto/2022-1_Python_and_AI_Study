cube = lambda x :x**3 # complete the lambda function 



def fibonacci(n):
    if n <2:
        c=0
        d=[]
        for i in range(0,n):
           
           d.append(c) 
    else:    
            a=0
            b=1 
            c=0
            d=[a,b]
            for i in range(n-2):
                c=a+b
                a=b
                b=c
                d.append(c)
    return d
        
        
    # return a list of fibonacci numbers

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
