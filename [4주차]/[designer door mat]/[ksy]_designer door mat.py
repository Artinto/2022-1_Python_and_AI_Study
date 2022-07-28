#designer door mat
a,b=input().split()
a=int(a)
b=int(b)
a=a//2
design=".|."
welcome="WELCOME"
for i in range(a,-a-1, -1):  
    if i==0:    
        print(welcome.center(b,'-'))
    else:   
        string1 = design*((a-abs(i))*2+1)
        print(string1.center(b, '-'))
