class Solution:
    def totalNQueens(self, n: int) -> int:
        board = [["."] * n for _ in range(n)]
        result = []
        response = 0
        def is_safe(board, r, c):
            # Column
            for row in range(r):
                if board[row][c] == "Q":
                    return False
            # Top-left diagonal
            row, col = r - 1, c - 1
            while row >= 0 and col >= 0:
                if board[row][col] == "Q":
                    return False
                row -= 1
                col -= 1
            # Top-right diagonal
            row, col = r - 1, c + 1
            while row >= 0 and col < n:
                if board[row][col] == "Q":
                    return False
                row -= 1
                col += 1
            return True

        
        def queens(row):
            nonlocal  response
            if row == n:
                response+=1
                return 
            for col in range(n):
                if is_safe(board, row, col):
                    board[row][col] = "Q"
                    queens(row + 1)
                    board[row][col] = "."

        queens(0)
        return response
