#!/bin/python3

import math
import os
import random
import re
import sys
import time

#
# Complete the 'runningTime' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def runningTime(arr):
    a=0#a를 0으로 두고 시작
    for i in range(1,len(arr)):#1부터 arr의 길이까지 반복
        b=arr[i]#b를 특정 숫자의 arr로 설정
        while arr[i-1]>b and i>0:#이 조건 동안
             arr[i-1], arr[i] = arr[i], arr[i-1]#arr[i-1]을 arr[i]로 arr[i]를 arr[i-1]로 설정
             i-=1#특정숫자 i를 1씩 감소시키면서 반복
             a+=1#a의 값을 1씩 증가시킨다
        arr[i]=b# 그 후에 arr[i]를 b로 바꿔서 값 나오게 해준다
    return a#a를 반복


    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = runningTime(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
