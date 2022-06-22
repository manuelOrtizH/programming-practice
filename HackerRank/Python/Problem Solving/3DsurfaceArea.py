#Manuel Ortiz at 2022
#Extracted from: https://www.hackerrank.com/challenges/3d-surface-area/problem

from functools import reduce
def surfaceArea(A,H,W):
    B = [list(map(lambda a: a[i], A)) for i in range(len(A[0]))]
    tb,l,r,f,b = 2*(W*H),sum(A[0]), sum(A[-1]), sum(B[0]), sum(B[-1])
    price = tb+l+r+f+b
    if H>1:
        for i in range(H-1):
            price+= sum(map(lambda a: abs(a[0] - a[1]), zip(A[i],A[i+1]) ))
    if W>1:
        for j in range(W-1):
            price+= sum(map(lambda a: abs(a[0] - a[1]), zip(B[j],B[j+1]) ))
    
    return price

if __name__ == '__main__':
    H,W=3,3
    A = [[1,3,4],[2,2,3],[1,2,4]]
    result = surfaceArea(A,H,W)
    print(result)