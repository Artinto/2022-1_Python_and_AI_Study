import math
import os
import random
import re
import sys

def countingSort(arr):
    count=[0]*100#*arr의 길이와 같은 count 배열을 만들어준다
    for i in range(len(arr)):#arr의 길이 만큼 반복을 수행
        count[arr[i]]+=1#숫자 i가 배열에 몇개가 존재하는 지 세도록 함수 생성
    return count#반복한다
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
