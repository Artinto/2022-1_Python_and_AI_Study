import math
import os
import random
import re
import sys

def insertionSort2(n, arr):
    for i in range(1, n):
        j = i
        while j > 0 and arr[j] < arr[j - 1]:
            a = arr[j]
            arr[j] = arr[j - 1]
            arr[j - 1] = a
            j -= 1
        print(*arr)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
