#Manuel Ortiz at 2022
#Extracted from: https://leetcode.com/problems/search-a-2d-matrix/

def searchMatrix(matrix, target):
    i = 0
    j = len(matrix[0]) - 1 
    while i < len(matrix) and j >= 0:
        value = matrix[i][j]
        if target == value:
            return True
        if target > value:
            i+=1
        else:
            j-=1
    return False


# matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
matrix = [[1,3]]
res = searchMatrix(matrix, 3)
print(res)