import math
import os
import random
import re
import sys

def runningTime(arr):
    z = 0
    for i in range(1, n):
        j = i
        while j > 0 and arr[j] < arr[j - 1]:
            a = arr[j]
            arr[j] = arr[j - 1]
            arr[j - 1] = a
            j -= 1
            z += 1
    return z

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = runningTime(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
