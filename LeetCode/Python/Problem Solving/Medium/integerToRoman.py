#Manuel Ortiz at 2022
#Extracted from: https://leetcode.com/problems/integer-to-roman/

I,V,X,L,C,D,M = 'I','V','X','L','C','D','M'
SYMBOLS = {1: I, 5: V, 10: X, 50: L, 100: C, 500: D, 1000: M}
import math

def intToRoman(num):
    log10 = lambda num: int(math.log10(num))
    div = lambda num,n: (num//(10**n)) * (10**n)
    n,s = 0, ''
    while (num-n)>0:
        num = num - n
        l = log10(num)
        n = div(num, l)
        if n in SYMBOLS:
            s+=SYMBOLS[n]
            continue
        a,b = 10**l, (10**(l+1))
        half = b//2
        if (n<(half-a) or n>half) and n<(b-a):
            times = (n//a)%5
            s+= SYMBOLS[a]*times if not n>half else SYMBOLS[half]+(SYMBOLS[a]*times)
            continue
        diff = (b-n)
        s += (SYMBOLS[diff] + SYMBOLS[diff*10]) if diff in SYMBOLS else (SYMBOLS[half-n] + SYMBOLS[half])
  
    return s

intToRoman(60)