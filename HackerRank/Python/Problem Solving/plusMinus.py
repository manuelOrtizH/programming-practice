# Manuel Ortiz Hernández at 2020
# Problem solving. Extracted from: https://www.hackerrank.com/challenges/plus-minus/problem
import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plus_minus(arr):
    results = {"Positive": 0, "Negative": 0, "Zero": 0}
    i = 0
    while i < len(arr):
        if arr[i] == 0:
            results["Zero"] += 1
        elif arr[i] > 0:
            results["Positive"] += 1
        else:
            results["Negative"] += 1
        i+=1

    return results
    

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    results = plus_minus(arr)

    print(results["Positive"]/n)
    print(results["Negative"]/n)
    print(results["Zero"]/n)