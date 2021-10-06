# Manuel Ortiz Hernández at 2020
#Problem solving. Extracted from: https://www.hackerrank.com/challenges/birthday-cake-candles/problem
import math
import os
import random
import re
import sys

def birthday_cake_candles(ar):
    i = 0
    maximum = 1
    counter = 0
    if not ar:
        return "empty"
    while i < len(ar):
        if ar[maximum] < ar[i]:
            maximum = i
            counter = 0
        if ar[maximum] == ar[i]:
            counter += 1
        i+=1
    return counter
        
if __name__ == '__main__':
    ar_count = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = birthday_cake_candles(ar)
    print(result)


