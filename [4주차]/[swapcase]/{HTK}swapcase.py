def swap_case(s):
    return s.swapcase()#swap case를 이용해변환이 생성된후 새 문자열 생성
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
