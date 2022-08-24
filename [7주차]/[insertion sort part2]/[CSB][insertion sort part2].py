import math
import os
import random
import re
import sys


def insertionSort2(n, arr):
  i=1
  j=1
  while(j<n):
    i=j
    target = arr[j]
    while(target<arr[i-1])and(i>0):
      arr[i]=arr[i-1]
      arr[i-1]=target
      i-=1
    print(*arr)
    j+=1


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
