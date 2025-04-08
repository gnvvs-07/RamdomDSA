class Solution:
    def isSafe(self, row, col, board, n):
        r, c = row, col
        while r >= 0 and c >= 0:
            if board[r][c] == 'Q':
                return False
            r -= 1
            c -= 1
        c = col
        while c >= 0:
            if board[row][c] == 'Q':
                return False
            c -= 1
        r, c = row, col
        while r < n and c >= 0:
            if board[r][c] == 'Q':
                return False
            r += 1
            c -= 1
        return True
    def solve(self, col, board, ans, n):
        if col == n:
            ans.append(list(board))
            return
        for row in range(n):
            if self.isSafe(row, col, board, n):
                board[row] = board[row][:col] + 'Q' + board[row][col+1:]
                self.solve(col + 1, board, ans, n)
                board[row] = board[row][:col] + '.' + board[row][col+1:]

    def solveNQueens(self, n):
        ans = []
        board = ['.' * n for _ in range(n)]
        self.solve(0, board, ans, n)
        return ans
