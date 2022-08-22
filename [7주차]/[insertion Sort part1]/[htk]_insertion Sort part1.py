#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    for i in range(1,len(arr)):#1부터 len(arr)까지 반복
        a=arr[i]#arr[i]를 현재 값으로 설정
        while i>0 and arr[i-1]>a:#i가 음수가 아니고 i 이전의 값이 a보다 크다면 서로의 값을 교환해준다
            arr[i]=arr[i-1]
            i-=1#i를 1씩 줄여가면서 이를 반복한다.
            print(*arr)#위의 조건을 통해 나온 arr을출력
        arr[i]=a#바꾼 arr[i]를다시 현재 값으로 설정
    print(*arr)#다시 바꾼 arr[i]까지 괄호 없이 출력
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)

