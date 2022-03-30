#Manuel Ortiz at 2022
#Extracted from https://www.hackerrank.com/challenges/strange-advertising/problem

import math

def viralAdvertising(n):
    total = 0
    initial = 5
    for i in range(n):
        likes = math.floor(initial/2)
        initial = likes * 3
        total += likes        
    return total

if __name__ == '__main__':
    n = 3
    result = viralAdvertising(n)
    print(result)