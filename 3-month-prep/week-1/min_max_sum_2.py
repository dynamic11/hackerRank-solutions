#!/bin/python3

import math
import os
import random
import re
import sys
   
#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#
def miniMaxSum(arr):
    min=max=sum=arr[0]
    
    for item in arr[1:]:
        if(item>max):
            max=item
        elif(item<min):
            min=item
            
        sum += item

    return [sum-max, sum-min]
    
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    result=miniMaxSum(arr)
    
    print(result[0],result[1])
