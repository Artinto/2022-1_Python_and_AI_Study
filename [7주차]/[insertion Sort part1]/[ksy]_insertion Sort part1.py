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

def printList(arr):
    for i in range(0, len(arr)):
        print(arr[i], end='')
        print(' ', end='')    
    print('')



def insertionSort1(n, arr):
    # Write your code here
    a=arr[n-1]
    for i in range(n-1):
        if a<arr[n-i-2]:
            arr[n-i-1]=arr[n-i-2]
            printList(arr)
            
        else:
            arr[n-i-1]=a
            printList(arr)
            return 0
    arr[0]=a
    printList(arr)
    return 0
            

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
            
