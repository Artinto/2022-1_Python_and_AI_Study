def swap_case(A):
    B = "" # 문자열 생성
    for i in A: 
        if i.isupper(): 
            B += i.lower() 
        elif i.islower(): 
            B += i.upper() 
        else:
            B += i
    return B



if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
