.Intro to Tutorial Challenges
import math
import os
import random
import re
import sys

def introTutorial(V, arr):
    return arr.index(V)#arr에서 v의 위치를 찾을 수있도록 index함수를 이용
    
    
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    V = int(input().strip())

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = introTutorial(V, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
