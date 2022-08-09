
def fibonacci(n):
    num = [0,1]
    for _ in range(n-2):
        fir, sec = num[-2], num[-1]
        fir, sec = sec, fir + sec         
        num.append(sec)
    return num

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
