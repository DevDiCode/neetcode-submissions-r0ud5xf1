class Solution:
    def solve(self, board: List[List[str]]) -> None:

        rows = len(board)
        cols =  len(board[0])

        def is_move(r,c):
            return r in range(rows) and \
                    c in range(cols) and \
                    board[r][c]=="O"



        


        def dfs(r,c):


            board[r][c]="T"

            directions = [(0,1),(1,0),(-1,0),(0,-1)]


            for dr, dc in directions:
                new_row, new_col = r + dr, c + dc

                if is_move(new_row, new_col):
                    dfs(new_row, new_col)
            
                # Start from the first and last row
        for i in range(rows):
            if board[i][0] == "O":
                dfs(i, 0)
            if board[i][cols - 1] == "O":
                dfs(i, cols - 1)

        # Start from the first and last column
        for j in range(cols):
            if board[0][j] == "O":
                dfs(0, j)
            if board[rows - 1][j] == "O":
                dfs(rows - 1, j)
            
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "T":
                    board[i][j] = "O"


        

