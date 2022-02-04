# Manuel Ortiz at 2022
# Extracted from:  https://www.hackerrank.com/challenges/drawing-book/problem

def pageCount(n,p):
    l = p//2
    r = n//2 - (p//2)
    print('The min is: ', min(l,r))

if __name__ == '__main__':
    n = 10
    p = 4
    pageCount(n, p)