def print_rangoli(size):
    # your code goes here
    import string # 파이썬에서 정의해놓은 모듈을 사용하기 위해 string 선언
    Alpha = string.ascii_lowercase # 소문자 데이터를 가져오기 위한 상수 (string 모듈)
    width = 4 * size - 3
    for i in list(range(size))[::-1] + list(range(1,size)): # [::-1]: 처음부터 끝까지 -1칸 간격으로 (= 역순으로)
        print('-'.join(Alpha[size-1:i:-1] + Alpha[i:size]).center(width,'-')) # size-1에서 i까지 역순으로 배열한 것과 i부터 size까지 배열한 것을 합친 후 width의 센터에 배치

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
