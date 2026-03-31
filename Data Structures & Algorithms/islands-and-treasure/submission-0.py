class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        directions = [(1,0),(0,1),(-1,0),(0,-1)]


        
        rows = len(grid)

        cols = len(grid[0])


        def is_move(r,c):
            return 0<=r<rows and 0<=c<cols and grid[r][c]==2147483647



        q = deque()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==0:
                    q.append((i,j,0))


        
        while q:
            for i in range(len(q)):
                r,c, dist = q.popleft()

                for dr , dc in directions:
                    new_row = r+dr
                    new_col = c + dc
                    if is_move(new_row,new_col):
                        grid[new_row][new_col] = dist+1
                        q.append((new_row,new_col,dist+1))

    