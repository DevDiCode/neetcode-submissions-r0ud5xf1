from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.max_area = 0

        def move(r, c):
            return 0 <= r < self.rows and 0 <= c < self.cols and grid[r][c] == 1

        def helper(r, c):
            if not move(r, c):
                return 0

            # Mark the cell as visited by setting it to None (or 0)
            grid[r][c] = 0
            count = 1

            # Possible directions: right, down, up, left
            directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

            for dr, dc in directions:
                new_row = r + dr
                new_col = c + dc
                count += helper(new_row, new_col)

            return count

        for r in range(self.rows):
            for c in range(self.cols):
                if grid[r][c] == 1:
                    self.max_area = max(self.max_area, helper(r, c))

        return self.max_area
