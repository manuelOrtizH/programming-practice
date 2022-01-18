#Manuel Ortiz at 2022
#Problem solving. Extracted from: https://www.hackerrank.com/challenges/the-birthday-bar/problem
import functools
import numpy as np

def birthday(choc_bar,day_sum,month):
    return np.array_split(choc_bar, 3)

if __name__ == '__main__':
    n = 5
    choc_bar = [2,2,1,3,2]
    day_sum = 4 #day sum
    month = 2 #month length
    splited = birthday(choc_bar, day_sum, month)
    for arr in splited:
        print(list(arr))