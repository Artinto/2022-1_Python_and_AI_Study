#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    
    a=s.split(" ")
    b=[]
    for i in range(len(a)):
        
        if a[i].isalpha()==True:
            new=a[i].title()
        else:
            new=a[i].capitalize()
        b.append(new)
        join_text=' '.join(b)
    return join_text

     
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
