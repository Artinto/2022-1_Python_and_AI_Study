#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'runningTime' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#


        
def runningTime(arr):
    n=len(arr)
    count=0 
    for i in range(1, n): 
        
        a = i+1
        
        for j in range(1, a):
            if arr[a-j] < arr[a-j-1]:
                nSwap = arr[a-j]
                arr[a-j] = arr[a-j-1]
                arr[a-j-1] = nSwap
                count+=1
            else:
                break
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = runningTime(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
