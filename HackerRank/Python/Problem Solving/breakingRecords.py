# Manuel Ortiz Hernández at 2021
# Problem solving. Extracted from: https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem
import math
import os
import random
import re
import sys

def breakingRecords(scores):
    to_beat = scores[0]
    times_up = 0
    times_down = 0
    records = {'Scores': scores, 'Highest': to_beat, 'Lowest': to_beat}
    for num in scores[1:]:
        if num > records['Highest']:
            records['Highest'] = num
            times_up += 1
        if num < records['Lowest']:
            records['Lowest'] = num
            times_down += 1
    result = [times_up, times_down]
    return result[0], result[1]

def readData():
    n = int(input())
    scores = list(map(int, input().rstrip().split()))
    return scores

def main():
    scores = [3, 4, 21, 36, 10, 28, 35, 5, 24, 42]
    # scores = readData()
    print("The result is: ", breakingRecords(scores))
    
if __name__ == '__main__':
    main()

    
