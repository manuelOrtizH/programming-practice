#Manuel Ortiz at 2022
#Extracted from: https://www.hackerrank.com/challenges/array-left-rotation/problem

def rotateLeft(d, arr):
    l = len(arr)
    result = [0]*l
    for i in range(l):
        new_pos = (l + (i-d)) - l
        result[new_pos] = arr[i]
    return result

if __name__ == '__main__':
    d = 7
    arr = [98, 67, 35, 1, 74, 79, 7, 26, 54, 63, 24, 17, 32, 81]
    result = rotateLeft(d,arr)
    print(result)