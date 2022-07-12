def is_leap(year): #이미 주어진 것. 함수 is_leap(year) 정의
    leap = False #이미 주어진 것. leap에 거짓 대입.
    if year>=1900 and year<=100000: #year가 1900와 같거나 크고 100000과 같거나 작을 때 수행한다.
        if year%4==0: #year을 4로 나눈 나머지가 0이면
            leap=True #leap에 참 대입.
        if year%100==0: #year을 100으로 나눈 나머지가 0이면
            leap=False #leap에 거짓 대입.
        if year%400==0: #year을 400dmfh 나눈 나머지가 0이면
            leap=True #leap에 참 대입.
        return leap #leap값 반환
year = int(input()) #year에 입력값 대입
print(is_leap(year)) #참인지 거짓인지 출력
