def print_rangoli(size):    # def 함수이름 (입력)
    fullAPB = 'abcdefghijklmnopqrstuvwxyz'  # 전체 알파벳 저장

    for i in range(size-1,-size,-1):    # 역순            
        A = '-'.join(fullAPB[size-1:abs(i):-1]+fullAPB[abs(i):size]) # 슬라이싱/ A 에 .join함수 이용하여 반환한 문자열 저장
        print(A.center(4*size-3,'-'))  # 문자열.center(출력할 문자열 길이,'추가할 문자') 출력

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
