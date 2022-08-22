#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort2' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort2(n, arr):
    for i in range(1,n):#n까지 반복한다.
        for j in range(0,i+1):#i+1까지 반복을 해준다
            if arr[j]>arr[i]:#만약 i안에서 j의 값이 arr[i]보다 크다면 arr[j]를 arr[i]로 바꿔준다.
                a=arr[j]
                arr[j]=arr[i]
                arr[i]=a#바꾼 arr[i]를다시 현재 값으로 설정
        print(*arr)#괄호없이 결과값 arr을 출력한다
                
            



if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)

