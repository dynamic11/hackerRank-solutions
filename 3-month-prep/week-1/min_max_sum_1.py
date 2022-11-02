#!/bin/python3

import math
import os
import random
import re
import sys


def min_sum(sortedArr):
    sum=0
    for index in range(4):
        sum += sortedArr[index]

    return sum

def max_sum(sortedArr):
    sum=0
    for index in range(4):
        arrayIndex = len(sortedArr)-index-1
        sum += sortedArr[arrayIndex]

    return sum
    
#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#
def miniMaxSum(arr):
    sortedArray=sorted(arr)
    print(min_sum(sortedArray), max_sum(sortedArray))
    
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
