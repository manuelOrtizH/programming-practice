#Manuel Ortiz at 2022
#Extracted from: https://www.hackerrank.com/challenges/equality-in-a-array/problem

from collections import Counter

def equalizeArray(arr):
    el_dict = Counter(arr)
    return len(arr) - max(Counter(arr).values())
    
if __name__ == '__main__':
    arr =  [3, 3, 2, 1, 3]
    result = equalizeArray(arr)
    print(result)