import math
import os
import random
import re
import sys

def insertionSort1(n, arr):
    a = arr[n - 1]
    b = n - 2
    while b >= 0 and arr[b] > a:
        arr[b + 1] = arr[b]
        print(*arr)
        b -= 1
    arr[b + 1] = a
    print(*arr)
        

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
