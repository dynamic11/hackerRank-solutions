#!/bin/python3

import math
import os
import random
import re
import sys


def pangrams(s):
    letters_count = dict()
    result = "not pangram"

    for letter in s:
        letter = letter.lower()
        if(letter != ' '):
            if letter in letters_count:
                letters_count[letter] += 1
            else:
                letters_count[letter] = 1

            if(len(letters_count) == 26):
                result = "pangram"
                break

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
