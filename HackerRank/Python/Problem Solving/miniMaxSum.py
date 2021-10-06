# Manuel Ortiz Hernández at 2020
#Problem solving. Extracted from: https://www.hackerrank.com/challenges/mini-max-sum/problem
import math
import os
import random
import re
import sys

def mini_max_sum(arr):
    maximum = 1
    minimum = 1
    total_sum = 0
    i = 0

    if not arr:
        return "empty"
    
    while i < len(arr):
        if arr[maximum] < arr[i]:
            maximum = i
        if arr[minimum] > arr[i]:
            minimum = i
        total_sum += arr[i]
        i+=1
    
    minimum = total_sum - arr[minimum]
    maximum = total_sum - arr[maximum] 
    
    print(maximum, minimum)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    mini_max_sum(arr)
