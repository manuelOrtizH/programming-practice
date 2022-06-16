#Manuel Ortiz at 2022
#Extracted from: https://www.hackerrank.com/challenges/save-the-prisoner/problem

import math
def saveThePrisoner(n, m, s):
    total_distributions = m + (s-1)
    laps = total_distributions / n
    remaining = math.floor(laps)
    if (laps % n != 0 or laps > n):
        remaining = total_distributions - (remaining * n)
    return remaining if remaining != 0 else n

if __name__ == '__main__':
    n,m,s = 2,8,1
    result = saveThePrisoner(n,m,s)
    print('Warn the Prisoner:', result)
    