n = int(input()) # n이라는 변수에 input값을 받는다.
if n>=1 and n<=20: # n이 1과 같거나 크고 20과 같거나 작을때 코드를 수행한다.
    for i in range(n): # i이 n의 범위내에 있을 동안
        print(i*i) # i^2를 출력한다
