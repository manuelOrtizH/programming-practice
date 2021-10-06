# Manuel Ortiz Hernández at 2020
#Problem solving. Extracted from: https://www.hackerrank.com/challenges/compare-the-triplets/problem
import math
import os
import random
import re
import sys

def compare_triplets(a,b):
    result_array = [0,0]
    for i in range(len(a)):
        if a[i] < b[i]:
            result_array[1]+=1
        elif a[i] > b[i]:
            result_array[0]+=1

    return result_array

if __name__ == '__main__':
    
    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compare_triplets(a, b)

    print(result)