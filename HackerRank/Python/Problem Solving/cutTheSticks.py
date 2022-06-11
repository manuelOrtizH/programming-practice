#Manuel Ortiz at 2022
#Extracted from: https://www.hackerrank.com/challenges/cut-the-sticks/problem

def cutTheSticks(arr):
    res = [len(arr)]
    arr = sorted(arr)
    actual_value = arr[0]
    counter = 0
    for el in arr:
        if el!= actual_value:
            actual_value = el
            res.append(res[0] - counter)
        counter+=1
    return res

if __name__ == '__main__':
    arr = [1,2,3,4,3,3,2,1]
    result = cutTheSticks(arr)
    print(result)