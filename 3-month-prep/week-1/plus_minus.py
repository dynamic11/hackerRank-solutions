#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plus_minus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plus_minus(arr):
    numbOfPos=0
    numbOfNeg=0
    arrayLength=len(arr)
    
    # Write your code here
    for number in arr:
        if number>0:
            numbOfPos+=1
        elif number<0:
            numbOfNeg+=1
    
    
    print("{0:.6f}".format(numbOfPos/arrayLength))
    print("{0:.6f}".format(numbOfNeg/arrayLength))
    print("{0:.6f}".format((arrayLength-(numbOfPos+numbOfNeg))/arrayLength))
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plus_minus(arr)
