#Manuel Ortiz at 2022
#Extracted from: https://www.hackerrank.com/challenges/sherlock-and-squares/problem

import math
def squares(a, b):
    diff,counter = 0,0
    if a == b:
        counter = 1 if math.sqrt(a) % 1 == 0 else 0
    while a<b:
        c = math.sqrt(a)
        if c % 1 == 0:
            diff = 2*c-1
            break
        a+=1
    if a < b:
        while a <= b:
            diff+=2
            a+=diff
            counter+=1
                        
    return counter

if __name__ == '__main__':

    a,b = 4,4
    result = squares(a,b)
    print(result)

