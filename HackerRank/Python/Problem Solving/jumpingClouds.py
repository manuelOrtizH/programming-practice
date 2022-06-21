#Manuel Ortiz at 2022
#Extracted from: https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem

def jumpingOnClouds(c):
    jumps = 0
    k = len(c)
    step = 2 if k>2 else 1
    while step<k:
        if c[step]==1:
            step-=1
        step=step+1 if (step+2)>=k else step+2
        jumps+=1
    return jumps

if __name__ == '__main__':
    c = [0, 0, 1, 0,
         0, 0, 0, 1,
         0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0,
         1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 
         0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 
         0, 1, 0, 1, 0, 0]
    result = jumpingOnClouds(c)
    print('JUMPS: ', result)