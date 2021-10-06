# Manuel Ortiz Hernández at 2020
#Problem solving. Extracted from: https://www.hackerrank.com/challenges/simple-array-sum/problem
import os
import sys

def simple_array_sum(array):
    sum_result = 0
    i = 0
    while i < len(array):
        sum_result+= array[i]
        i+=1

    return sum_result


if __name__ == '__main__':
    
    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = simple_array_sum(ar)

    print(result)

