def print_formatted(number):
    w=len(bin(number)[2:])
    # your code goes here
    for i in range(1,number+1):
        b = format(i, 'b')            # 10 to 2
    
        o = format(i, 'o')            # 10 to 8

        h = format(i, 'X')
        i=str(i)
        b=str(b)
        o=str(o)
        h=str(h)            # 10 t0 16   

        print(i.rjust(w,' '),o.rjust(w,' '),h.rjust(w,' '),b.rjust(w,' '))
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
