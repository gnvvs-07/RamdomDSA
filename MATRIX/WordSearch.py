# LeetCode 79 :https://leetcode.com/problems/word-search/description/

# Given an m x n grid of characters board and a string word, return true if word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# Output: true

# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
# Output: true

# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
# Output: false

# task-1 : finding the first element which matches in the target and matrix



def search_first(matrix,word):
    rows = len(matrix)
    cols = len(matrix[0])
    index = 0
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == word[index]:
                # task -2:searching the next upcomming characters
                if searchNext(matrix,word,i,j,index,rows,cols):
                    return "true"
    return "false"
                

def searchNext(matrix,word,i,j,ind,rows,cols):
        if ind == len(word):
              return True
        if i < 0 or j < 0 or i == rows or j == cols or matrix[i][j] !=word[ind] or matrix[i][j] == '*':
            return False
        current_character = matrix[i][j]
        dummy = "*"
        matrix[i][j] = dummy
        # top
        top = searchNext(matrix,word,i-1,j,ind+1,rows,cols)
        # down
        down = searchNext(matrix,word,i+1,j,ind+1,rows,cols)
        # left
        left = searchNext(matrix,word,i,j-1,ind+1,rows,cols)
        # right
        right = searchNext(matrix,word,i,j+1,ind+1,rows,cols)

        matrix[i][j] = current_character

        return top or down or left or right


board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCB"

print(search_first(board,word))