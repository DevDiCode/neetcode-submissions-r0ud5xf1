class Solution:
    def solve(self, board: List[List[str]]) -> None:

        rows = len(board)
        cols = len(board[0])

        def is_move(r,c):

            return 0 <= r < rows and 0 <= c < cols and board[r][c] == "O"

        def dfs(r,c):
            
            if not is_move(r,c):
                return 

            board[r][c]="E"

            directions = [(1,0),(0,1),(-1,0),(0,-1)]

            for dr, dc in directions:

                dfs(r+dr,c+dc)

        #check border rows

        for j in range(cols):
            if board[0][j]=="O":
                dfs(0,j)

            if board[rows-1][j]=="O":
                dfs(rows-1,j)


    

        #check border cols
        for i in range(rows):
            if board[i][0]=="O":
                dfs(i,0)
            
            if board[i][cols-1]=="O":
                dfs(i,cols-1)

                # Flip the remaining 'O's to 'X' and 'E' back to 'O'
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "E":
                    board[i][j] = "O"


