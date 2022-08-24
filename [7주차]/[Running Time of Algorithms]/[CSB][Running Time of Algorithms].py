import math
import os
import random
import re
import sys


def runningTime(arr):
    shift=0
    i=1
    j=1
    while(j<n):
        i=j
        target = arr[j]
        while(target<arr[i-1])and(i>0):
            arr[i]=arr[i-1]
            arr[i-1]=target
            i-=1
            shift+=1
        j+=1
    return shift

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = runningTime(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
