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
    # Write your code here
    for i in range(2,len(arr)+1,1):
        arr2=arr[0:i:1]
        arr2.sort()
        arr[0:i]=arr2
        result=' '.join(map(str,arr))
        print(result)
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
