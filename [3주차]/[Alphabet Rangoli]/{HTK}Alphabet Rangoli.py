def print_rangoli(size):
    # your code goes here
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(size-1,-size,-1):
        #범위를 range로 역순으로 준다
        z = '-'.join(alphabet[size-1:abs(i):-1]+alphabet[abs(i):size])
        # 그 이후에 join함수를 이용해 알파벳을 서로 묶을수 있게
        print(z.center(4*size-3,'-'))
        #center함수를 이용해서 가로 세로를 구함
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
