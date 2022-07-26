import cmath
z = complex(input())
print(cmath.polar(z)[0])
print(cmath.polar(z)[1])
# cmath.polar() : (절대값, 편각) 튜플

import cmath
z = complex(input())
print(abs(z)) # abs() : 복소수의 절대값
print(cmath.phase(z)) # phase() : 적위(위상)
