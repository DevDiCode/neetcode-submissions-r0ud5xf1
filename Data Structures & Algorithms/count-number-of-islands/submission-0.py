class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        

        count = 0 
        rows = len(grid)
        cols = len(grid[0])

        def isMove(r,c):
            return 0<=r<rows and 0<=c<cols and grid[r][c]=="1"

        def dfs(r,c):
            
            grid[r][c]="0"

            directions = [(1,0),(0,1),(-1,0),(0,-1)]
            for dr, dc in directions:
                new_row = r+dr 
                new_col = c+dc
                if isMove(new_row,new_col):
                    dfs(new_row,new_col)


        for i in range(rows):
            for j in range(cols):
                if grid[i][j]=="1":
                    dfs(i,j)
                    count+=1
        
        return count


        


        

    
