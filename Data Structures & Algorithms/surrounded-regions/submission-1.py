from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:  # Edge case: Empty board
            return

        rows, cols = len(board), len(board[0])

        def isMove(r, c):
            """Check if the move is within bounds and is an 'O'."""
            return 0 <= r < rows and 0 <= c < cols and board[r][c] == "O"

        def dfs(r, c):
            """DFS to mark connected 'O' cells as 'E' (escaped)."""
            board[r][c] = "E"  # Mark as escaped
            
            # Explore all four directions
            directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # Down, Right, Up, Left
            for dr, dc in directions:
                new_row, new_col = r + dr, c + dc
                if isMove(new_row, new_col):  # Check before calling DFS
                    dfs(new_row, new_col)  # Recursive DFS call

        # Step 1: Perform DFS from the borders to mark escape regions as 'E'
        for i in range(cols):  
            if isMove(0, i):  # First row
                dfs(0, i)
            if isMove(rows - 1, i):  # Last row
                dfs(rows - 1, i)

        for j in range(rows):
            if isMove(j, 0):  # First column
                dfs(j, 0)
            if isMove(j, cols - 1):  # Last column
                dfs(j, cols - 1)

        # Step 2: Convert the board
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O":
                    board[i][j] = "X"  # Captured region
                elif board[i][j] == "E":
                    board[i][j] = "O"  # Restore escaped regions
