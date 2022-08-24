import math
import os
import random
import re
import sys
import itertools

def countingSort(arr):
    narr = list(itertools.repeat(0, 100))
    for i in range(0, n):
        a = arr[i]
        narr[a] += 1
    return narr  

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
