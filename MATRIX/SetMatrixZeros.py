# Leet Code 73 : https://leetcode.com/problems/set-matrix-zeroes/description/

# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

# You must do it in place.

# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]

# Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
rows = len(matrix)
cols = len(matrix[0])
zero_rows = {i for i in range(rows) if 0 in matrix[i]}
zero_cols = {j for j in range(cols) if any(matrix[i][j] == 0 for i in range(rows))}

matrix = [
    [0 if i in zero_rows or j in zero_cols else matrix[i][j] for j in range(cols)]
    for i in range(rows)
]

for row in matrix:
    print(*row)