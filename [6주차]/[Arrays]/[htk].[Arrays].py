 import numpy

def arrays(arr):
    return numpy.array(arr[::-1],float)#입력된  arr를 거꾸로 뒤집기 위해 arr[::-1}을 입력후 이를 정수로 출력하기 위해 float을 사용
arr = input().strip().split(' ')
result = arrays(arr)
print(result)
