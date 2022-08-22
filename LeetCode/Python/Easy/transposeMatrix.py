#Manuel Ortiz at 2022
#Extracted from: https://leetcode.com/problems/transpose-matrix/

def transpose(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    transposed = [[0 for col in range(rows)] for row in range(columns)]
    for i in range(columns):
        for j in range(rows):
            element = matrix[j][i]
            transposed[i][j] = element
    return transposed
    

matrix = [[1,2,3],[4,5,6],[7,8,9]]
transpose(matrix)