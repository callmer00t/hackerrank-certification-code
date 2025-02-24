#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'findSum' function below.
#
# The function is expected to return a LONG_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY numbers
#  2. 2D_INTEGER_ARRAY queries
#

def findSum(numbers, queries):
    n = len(numbers)

    # Step 1: Compute prefix sum and zero count arrays
    prefix = [0] * (n + 1)
    zero_count = [0] * (n + 1)

    for i in range(1, n + 1):
        prefix[i] = prefix[i - 1] + numbers[i - 1]
        zero_count[i] = zero_count[i - 1] + (1 if numbers[i - 1] == 0 else 0)

    # Step 2: Process queries
    results = []
    for l, r, x in queries:
        subarray_sum = prefix[r] - prefix[l - 1]
        zero_addition = (zero_count[r] - zero_count[l - 1]) * x
        results.append(subarray_sum + zero_addition)

    return results

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    numbers_count = int(input().strip())

    numbers = []

    for _ in range(numbers_count):
        numbers_item = int(input().strip())
        numbers.append(numbers_item)

    queries_rows = int(input().strip())
    queries_columns = int(input().strip())

    queries = []

    for _ in range(queries_rows):
        queries.append(list(map(int, input().rstrip().split())))

    result = findSum(numbers, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
