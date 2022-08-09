from fractions import Fraction
from functools import reduce

def product(fracs):
    t =reduce(lambda x,y:x*y, fracs) # complete this line with a reduce statement#reduce 함수를 이용해서 x,y의 값을 x*y로 나타낸다 reduce함수는 왼쪽에서 오른쪽으로 두 값을 하나의 값으로 줄인다
    return t.numerator, t.denominator

if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)
