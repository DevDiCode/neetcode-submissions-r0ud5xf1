class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:


        response=0 

        rows = len(grid)
        cols = len(grid[0])

        visited = set()

        def is_move(r,c):

            return (r,c) not in visited and \
            r in range(rows) and  \
            c in range(cols) and  \
            grid[r][c] == "1"
        

        def dfs(r,c):
            
            visited.add((r,c))

            directions = [(1,0),(0,1),(-1,0),(0,-1)]

            for dr , dc in directions:

                if is_move(r+dr, c+dc):
                    dfs(r+dr, c+dc)

        for r in range(rows):
            for c in range(cols):

                if grid[r][c]=="1" and is_move(r,c):
                    dfs(r,c)
                    response+=1
        
        return response
        