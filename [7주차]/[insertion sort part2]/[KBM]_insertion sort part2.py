#!/bin/python3

import math
import os
import random
import re
import sys

def insertionSort2(n, arr):
    for i in range (1, n):        
        A = arr[i]
        while i > 0 and arr[i-1] > A:
        
            arr[i] = arr[i-1]
            i = i- 1
        arr[i] = A
        print(*arr)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
