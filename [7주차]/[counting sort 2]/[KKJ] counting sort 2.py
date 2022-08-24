import math
import os
import random
import re
import sys
import itertools

def countingSort(arr):
    narr = []
    for i in range(0, 100):
        a = arr.count(i)
        b = list(itertools.repeat(i, a))
        narr.extend(b)
    return narr
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
