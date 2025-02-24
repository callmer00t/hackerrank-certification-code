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
    # Convert string to list for easier manipulation
    password = list(s)
    i = 0
    # Store numbers at the beginning
    numbers = []
    
    # First, collect all leading numbers
    while i < len(password) and password[i].isdigit():
        numbers.append(password[i])
        i += 1
    
    # Remove the leading numbers from password
    password = password[i:]
    
    # Process the rest of the string
    i = 0
    while i < len(password):
        # Handle zero replacement
        if password[i] == '0':
            # Replace '0' with the last collected number
            password[i] = numbers.pop()
        
        # Handle swapped characters marked with '*'
        elif i + 2 < len(password) and password[i+2] == '*':
            # Swap back the characters
            password[i], password[i+1] = password[i+1], password[i]
            # Remove the '*'
            password.pop(i+2)
            i += 2
            continue
            
        i += 1
    
    # Convert list back to string
    return ''.join(password)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input().strip()

    result = decryptPassword(s)

    fptr.write(result + '\n')

    fptr.close()
