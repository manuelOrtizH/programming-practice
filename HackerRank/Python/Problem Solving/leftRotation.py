#Manuel Ortiz at 2022
#Extracted from: https://www.hackerrank.com/challenges/array-left-rotation/problem

def rotateLeft(d, arr):
    return [arr[i] for i in range(d,len(arr))] + [arr[i] for i in range(0,d)] 

if __name__ == '__main__':
    d = 7
    arr = [98, 67, 35, 1, 74, 79, 7, 26, 54, 63, 24, 17, 32, 81]
    result = rotateLeft(d,arr)
    print(result)