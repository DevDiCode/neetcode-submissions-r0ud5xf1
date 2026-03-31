from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        # Initialize the board as an n x n grid filled with '.'
        board = [["."] * n for _ in range(n)]

        result = []

        # Helper function to check if the position is safe
        def is_safe(board, r, c):
            # Check the column for any existing queen
            for row in range(r):
                if board[row][c] == "Q":
                    return False

            # Check the diagonal (top-left to bottom-right)
            row, col = r - 1, c - 1
            while row >= 0 and col >= 0:
                if board[row][col] == "Q":
                    return False
                row -= 1
                col -= 1

            # Check the diagonal (top-right to bottom-left)
            row, col = r - 1, c + 1
            while row >= 0 and col < n:
                if board[row][col] == "Q":
                    return False
                row -= 1
                col += 1

            return True

        # Helper function to solve N-Queens using backtracking
        def queens(board, row):
            if row == n:
                result.append(["".join(row) for row in board])  # Add a valid board solution
                return

            # Try to place a queen in each column of the current row
            for col in range(n):
                if is_safe(board, row, col):
                    board[row][col] = "Q"  # Place the queen
                    queens(board, row + 1)  # Recurse for the next row
                    board[row][col] = "."  # Backtrack

        queens(board, 0)  # Start solving from the first row
        return result
