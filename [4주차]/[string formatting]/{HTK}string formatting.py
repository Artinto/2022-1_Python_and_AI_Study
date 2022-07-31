def print_formatted(number):
    # your code goes here
    
    for i in range(1,number+1):
        a=str(i)#string함수를 이용해 그대로 출력
        b=oct(i)[2:]#10진수로
        c=hex(i)[2:].upper()#8진수 출력
        d=bin(i)[2:]#2진수로
        print(a.rjust(number),b.rjust(number),c.rjust(number),d.rjust(number))#모두 오른쪽 정렬
