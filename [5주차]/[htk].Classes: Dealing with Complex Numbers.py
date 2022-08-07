.import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real=real#첫번째 인자로 인스턴스를 전달하기 위해 self 함수를 사용해 real값 설정
        self.imaginary=imaginary#
        
    def __add__(self, no):
        a=(self.real+no.real)#
        b=(self.imaginary+no.imaginary)#self와 no의 각 허수와 실수를 더해서 a,b 값생성
        return complex(a,b) # 그후에 complex를 이용해 값 출력
        
    def __sub__(self, no):
        a=(self.real-no.real)
        b=(self.imaginary-no.imaginary))#self와 no의 각 허수와 실수를 빼서 a,b 값생성
        return complex(a,b)# 그후에 complex를 이용해 값 출력
        
    def __mul__(self, no):
        a=(self.real*no.real)
        b=(self.imaginary*no.imaginary)#self와 no의 각 허수와 실수를 곲해서 a,b 값생성
        return complex(a,b)# 그후에 complex를 이용해 값 출력

    def __truediv__(self, no):
        a=(self.real/no.real)
        b=(self.imaginary/no.imaginary)#self와 no의 각 허수와 실수를 나눠서 a,b 값생성
        return complex(a,b)# 그후에 complex를 이용해 값 출력
    def mod(self):
        e=math.sqrt(self.real**2+self.imaginary**2)#math.sqrt를 이용해서 안에서 생성된 숫자의 제곱근을 반환
        round(e,2)
        return complex(e,0)# 그후에 complex를 이용해 값 출력
    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.m
