def print_rangoli(size):
    import string
    letter = string.ascii_lowercase
    for i in range(size-1,-size,-1):           
        A = '-'.join(letter[size-1:abs(i):-1]+letter[abs(i):size])
        print(A.center(4*size-3,'-'))
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
    
# string.ascii_lowercase는 소문자로 abcd....wxyz를 의미한다.
# string.ascii_uppercase는 대문자로 ABCD...WXYZ를 의미한다.
