cube = lambda x: x**3# complete the lambda function 
def fibonacci(n):
    # return a list of fibonacci numbers
    c=[]
    a,b= 0,1#a,b를 각가 0과 1로 설정
    for i in range(1,n+1):#1부터 n+1까지 반복문 설정
        c.append(a) #이 때 c에 a의 값을 붙여준다
        a,b=b,a+b#b를 a+b로 하고 a는 이때의 b의 값이 나오도록 피보나치 수열 설정
    return c
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))      
