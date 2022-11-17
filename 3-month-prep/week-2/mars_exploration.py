#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'marsExploration' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#


def marsExploration(s):
    sos_string = "SOS"
    count = 0
    for i in range(len(s)):
        index_of_sos = i % len(sos_string)
        if(s[i] != sos_string[index_of_sos]):
            count += 1
    return count

    # Write your code here
    for letter, index in list(s):
        if(letter != "S" and letter != "O"):
            count += 1

    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
