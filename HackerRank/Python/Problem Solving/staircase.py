# Manuel Ortiz Hernández at 2020
#Problem solving. Extracted from: https://www.hackerrank.com/challenges/staircase/problem
import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    if n == 1:
        return "#"
    pattern = [(' '*(n-i) + '#'*(i)) for i in range(1,n+1)]
    print('\n'.join(pattern))
    

if __name__ == '__main__':
    n = int(input())
    staircase(n)
