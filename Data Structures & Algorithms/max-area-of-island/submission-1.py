class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:


        if not grid:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        visited = set()

        self.max_area = 0



        def isMove(r,c):
            return 0 <= r < rows and 0 <= c < cols and (r, c) not in visited and grid[r][c]==1

        def dfs(r,c):

            if not isMove(r,c):
                return 0

            area =1
            visited.add((r,c))


            directions = [(1,0),(0,1),(-1,0),(0,-1)]

            for dr, dc in directions:
                new_row , new_col = r+dr , c+dc
                area += dfs(new_row,new_col)

            return area



        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1 and (r,c) not in visited:
                    current_area = dfs(r,c)
                    self.max_area = max(self.max_area,current_area)


        return self.max_area
