# Manuel Ortiz Hernández at 2020
# Problem solving. Extracted from: https://www.hackerrank.com/challenges/diagonal-difference/problem
import math
import os
import random
import re
import sys

def diagonal_difference(arr):
    left_sum = 0
    right_sum = 0
    l = len(arr)-1
    i = 0
    while i < len(arr):
        left_sum += arr[i][i]
        right_sum += arr[i][l]
        print(l)
        l-=1
        i+=1
    return abs(left_sum - right_sum)

if __name__ == '__main__':
    
    n = int(input().strip())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonal_difference(arr)
    print(arr)
    print(result)
