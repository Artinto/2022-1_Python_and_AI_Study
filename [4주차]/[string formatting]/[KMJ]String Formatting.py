def print_formatted(number):
    l = []

    for i in range(1, n+1):
        decimal = str(i)
        octal = str(oct(i)[2:])
        Hexadecimal = str(hex(i)[2:])
        binary = str(bin(i)[2:])

        l.append([decimal, octal, Hexadecimal, binary])

    for i in l:
        print(*(number.rjust(len(results[-1][3])) for number in i))
        
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
    
    
# 리스트를 만들어 리스트 안에 차례대로 10, 8, 16, 2진법을 한 수를 넣는다.
# 리스트에 저장된 값들을 1부터 n까지 출력한다.
# 출력할때는 rjust를 이용하여 오른쪽에 하나씩 출력하는데, 이때 크기가 가장 큰 binary의 길이만큼 띄워쓰기를 해주기 위해 results[-1][3]를 사용한다.


def print_formatted(number):
    
    for i in range(1,n+1):
         print(i, oct(i)[2:], hex(i)[2:], bin(i)[2:], end=' ')

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
    
# 이건 틀린 코드.
# 저렇게 하면 간단하게 표현은 가능하지만 줄바꿈 없이 한번에 나열되고, 띄워쓰기가 무조건 한칸이다.
