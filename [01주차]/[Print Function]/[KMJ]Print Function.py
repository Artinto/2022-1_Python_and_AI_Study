n=int(input()) #n이라는 변수에 입력값을 받는다
if n<=150 and n>=1: #n이 1과 같거나 크고 150과 같거나 작을 때 수행한다
    for i in range(0,n): #i가 0에서 n까지 리스트를 만든다 (0~n의 범위 안에 있을 때 수행한다)
        print(i+1,end='') #end를 이용하여 줄바꿈없이 i+1를 출력한다.
       
#n이 5라면 i가 0부터 5까지 리스트를 만들어서 i+1를 출력하니 1,2,3,4,5를 출력한다.
