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

def insertionSort1(n, arr):
  a=arr[-1]
  while (n!=0):
    if n==1:
      arr[0]=a
      n=n-1
      result=' '.join(map(str,arr))
      print(result)
    else:
      arr[n-1]=arr[n-2]
      if arr[n-2]<a:
        arr[n-1]=a
        result=' '.join(map(str,arr))
        print(result) 
        break
      result=' '.join(map(str,arr))
      print(result)
    
      n=n-1




    
    


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
