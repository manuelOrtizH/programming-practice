#Manuel Ortiz at 2022
#Extracted from: https://www.hackerrank.com/challenges/picking-numbers/problem

def pickingNumbers(a):
    max_nums = 0
    res = [a[0]]
    for i in range(1, len(a)):
        if a[i] - a[i-1] <= 1 and a[i] - res[0] <=1:
            res.append(a[i])            
        else:
            res = [a[i]]
        max_nums = len(res) if max_nums <= len(res) else max_nums
    print(max_nums)
    return max_nums

if __name__ == '__main__':
    a = [1,1,2,2,4,4,5,5,5]
    pickingNumbers(sorted(a))