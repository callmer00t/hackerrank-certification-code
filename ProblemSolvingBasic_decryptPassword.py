 #!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'decryptPassword' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def decryptPassword(s):
    result = []
    i = 0
    while i < len(s):
        if i + 2 < len(s) and s[i].islower() and s[i + 1].isupper() and s[i + 2] == '*':
            # Step 1: Swap the lowercase and uppercase characters and remove '*'
            result.append(s[i + 1])
            result.append(s[i])
            i += 3  # Move past the swapped characters and '*'
        elif s[i] == 'o' and i - 1 >= 0 and s[i - 1].isdigit():
            # Step 2: If 'o' follows a digit, we need to restore the digit before 'o'
            result.append(s[i - 1])
            result.append('o')
            i += 1  # Move past the 'o'
        else:
            # Step 3: Just append the character and move on
            result.append(s[i])
            i += 1
    
    return ''.join(result)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input().strip()

    result = decryptPassword(s)

    fptr.write(result + '\n')

    fptr.close()
