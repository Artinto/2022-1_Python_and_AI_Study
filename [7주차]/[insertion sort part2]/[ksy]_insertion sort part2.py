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
def printList(arr):
    for i in range(0, len(arr)):
        print(arr[i], end='')
        print(' ', end='')    
    print('')

def insertionSort2(n, arr):
    for i in range(1, n):    
        a = i+1
        
        for j in range(1, a):
            if arr[a-j] < arr[a-j-1]:
                nSwap = arr[a-j]
                arr[a-j] = arr[a-j-1]
                arr[a-j-1] = nSwap
            else:
                break

        printList(arr)



if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
