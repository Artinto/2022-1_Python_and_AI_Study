import numpy

def arrays(arr):
    return(numpy.array(list(reversed(arr)), float))

arr = input().strip().split(' ')
result = arrays(arr)
print(result)

# numpy는 많은 양의 배열과 행렬을 정리하는데 사용한다.
# 주어진 문제에서는 numpy를 활용하여 입력을 float형태로 바꾸고 순서를 반대로 출력하는게 목표였으므로,
# return 반환을 이용하여 arrays(arr)을 리스트 형태로 바꾸고 reversed로 뒤집은 뒤 float형태를 취한다.
