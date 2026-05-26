class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid:
            return 0
            
        ROWS, COLS = len(grid), len(grid[0])
        count = 0
        
        # 1. Separated Validity Checker
        def is_move(r, c):
            # Returns True if within bounds AND it is unvisited land
            return 0 <= r < ROWS and 0 <= c < COLS and grid[r][c] == "1"

        def dfs(r, c):
            # 2. Base Case: Terminate if the move is invalid
            
            # 3. Mark as visited by "sinking" the island
            grid[r][c] = 0 

            
            # 4. Explore all 4 directions recursively
            directions = [(1,0), (-1,0), (0,1), (0,-1)]
            for dr, dc in directions:
                
                new_row , new_col = r+dr, c+dc

                if is_move(new_row,new_col):
                    dfs(new_row,new_col)
            
        # 5. Main traversal loop
        for r in range(ROWS):
            for c in range(COLS):
                # Only trigger DFS if we find an unvisited piece of land
                if grid[r][c] == "1":

                    count+=1

                   
                    dfs(r,c)

                    
        return count