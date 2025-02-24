#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'maxSubarrayValue' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def maxSubarrayValue(arr):
    n = len(arr)
    max_value = float('-inf')
    
    # Try all possible subarrays
    for i in range(n):
        even_sum = 0
        odd_sum = 0
        
        # For each starting point i, calculate values for all subarrays starting at i
        for j in range(i, n):
            # If current position (j-i) is even in the subarray
            if (j-i) % 2 == 0:
                even_sum += arr[j]
            # If current position (j-i) is odd in the subarray
            else:
                odd_sum += arr[j]
                
            # Calculate value for current subarray
            current_value = (even_sum - odd_sum) ** 2
            max_value = max(max_value, current_value)
    
    return max_value

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = maxSubarrayValue(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
