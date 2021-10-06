#Manuel Ortiz Hernández at 2020
#Problem Solving. Extracted from: https://www.hackerrank.com/challenges/apple-and-orange/problem

import math
import os
import random
import re
import sys

def countAppleAndOranges(s, t, a, b, apples, oranges):
    apple_counter = 0
    orange_counter = 0

    if not apples and not oranges:
        print(0,0,sep="\n")
        return

    apple_counter = getDistances(apples, a, s, t)
    orange_counter = getDistances(oranges, b, s, t)

    print(apple_counter,orange_counter, sep="\n")
    

def getDistances(fruits, pos, s, t):

    i = 0
    to_add = 0
    while i < len(fruits):
        fruits[i] = pos + fruits[i]

        if fruits[i] >= s and fruits[i] <= t:
            to_add +=1

        i+=1

    return to_add 
    

def readData():
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))
    input_dict = {'s': s, 't': t, 'a': a, 'b': b, 'apples': apples, 'oranges': oranges}

    return input_dict

    

def main():
    input_dict = readData()
    countAppleAndOranges(input_dict['s'], input_dict['t'], input_dict['a'], input_dict['b'], input_dict['apples'],
                         input_dict['oranges'])


if __name__ == '__main__':
    main()

