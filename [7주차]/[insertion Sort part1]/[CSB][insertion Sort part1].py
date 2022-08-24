import math
import os
import random
import re
import sys


def insertionSort1(n, arr):
    i = n-2
    A = arr[n-1]

    while (A < arr[i]) and (i >= 0):
        arr[i+1] = arr[i]
        print(*arr)
        i -= 1
    
    arr[i+1] = A
    print(*arr)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
