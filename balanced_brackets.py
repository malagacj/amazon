#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isBalanced function below.
def isBalanced(s):
    brackets = {')': '(', ']': '[', '}': '{'}
    openings = []
    closings = [')', ']', '}']

    length = len(s)
    if length % 2 != 0:
        return 'NO'

    for char in s:
        if char not in closings:
            openings.append(char)
            continue
        if not openings:
            return 'NO'
        if brackets[char] == openings[-1]:
            openings.pop(-1)

    if openings:
        return 'NO'
    else:
        return 'YES'

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)
        print(result)
