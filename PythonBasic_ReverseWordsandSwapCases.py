#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'reverse_words_order_and_swap_cases' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING sentence as parameter.
#

def reverse_words_order_and_swap_cases(sentence):
    # Split the sentence into words
    words = sentence.split()
    # Reverse the order of words
    reversed_words = words[::-1]
    # Swap the case of each character in the reversed sentence
    result = " ".join(reversed_words).swapcase()
    return result

if __name__ == '__main__':
    sentence = input().strip()
    print(reverse_words_order_and_swap_cases(sentence))
