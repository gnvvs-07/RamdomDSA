# Leetcode 212 wordSearch 2 : https://leetcode.com/problems/word-search-ii/description/

# Given an m x n board of characters and a list of strings words, return all words on the board.

# Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

# Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
# Output: ["eat","oath"]

def search_all(matrix,words,output = None):
    if output is None:
        output = []
    for word in words:
         if search_first(matrix,word):
            output.append(word)
    return output

def search_first(matrix,word):
    rows = len(matrix)
    cols = len(matrix[0])
    index = 0
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == word[index]:
                # task -2:searching the next upcomming characters
                # making a visited matrix for larger inputs
                visited = [[False for _ in range(cols)]for _ in range(rows)]
                if searchNext(matrix,word,i,j,index,rows,cols,visited):
                    return True
    return False
                

def searchNext(matrix,word,i,j,ind,rows,cols,visited):
        if ind == len(word):
              return True
        if i < 0 or j < 0 or i >= rows or j >= cols or matrix[i][j] !=word[ind] or visited[i][j]:
            return False
        visited[i][j] = True
        # top
        top = searchNext(matrix,word,i-1,j,ind+1,rows,cols,visited)
        # down
        down = searchNext(matrix,word,i+1,j,ind+1,rows,cols,visited)
        # left
        left = searchNext(matrix,word,i,j-1,ind+1,rows,cols,visited)
        # right
        right = searchNext(matrix,word,i,j+1,ind+1,rows,cols,visited)

        visited[i][j] = False

        return top or down or left or right


board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
words = ["oath","pea","eat","rain"]

print(search_all(board,words))



# -----------OPTIMAL YET TO BE DONE --------------