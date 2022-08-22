#Manuel Ortiz at 2022
#Extracted from: https://leetcode.com/problems/roman-to-integer/

I,V,X,L,C,D,M = 'I','V','X','L','C','D','M'
SYMBOLS = {I: 1, V: 5, X: 10, L: 50, C: 100, D: 500, M: 1000}
def romanToInt(s):
    n = SYMBOLS[s[-1]]
    for i in range(len(s)-2,-1,-1):
        actual, prev = SYMBOLS[s[i]], SYMBOLS[s[i+1]]
        n+=(-actual) if actual < prev else actual
    return n

romanToInt('IX')