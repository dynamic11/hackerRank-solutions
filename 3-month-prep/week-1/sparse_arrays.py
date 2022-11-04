#!/bin/python3

import math
import os
import random
import re
import sys


# this solution is O(n^2)
def matchingStrings(strings, queries):
    results = [0]*len(queries)
    for index, searchQuery in enumerate(queries):
        for string in strings:
            if(searchQuery==string):
                results[index] += 1
    return results

# this is a better solution that is O(n) and it uses dictionaries
def matchingStrings_v2(strings, queries):

    strings_dict = dict()

    for s in strings:                    
        if s in strings_dict:
            # If string is present in dictionary just increase its count        
            strings_dict[s] += 1   
        else:
            # Else just create a dictionary key for it and assign its apperance to 1                      
            strings_dict[s] = 1
    
    result = []

    # For each query find if the query string is in the dict
    for q in queries:                   
        if q in strings_dict:
            result.append(strings_dict[q])
        else:
            result.append(0)
    
    return result
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    strings_count = int(input().strip())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings_v2(strings, queries)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
