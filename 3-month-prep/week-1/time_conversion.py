#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def time_conversion(s):
    # Write your code here
    period = s[-2:]
    hours = s[0:2]

    if(hours == "12"):
        hours = '00'

    if(period == "PM"):
        hours = int(hours)+12

    return str(hours)+s[2:-2]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = time_conversion(s)

    fptr.write(result + '\n')

    fptr.close()
