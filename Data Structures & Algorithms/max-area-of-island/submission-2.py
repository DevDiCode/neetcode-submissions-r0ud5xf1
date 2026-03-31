from typing import List, Set, Tuple

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited: Set[Tuple[int, int]] = set()

        def is_move(r: int, c: int) -> bool:
            return (
                0 <= r < rows and
                0 <= c < cols and
                grid[r][c] == 1 and
                (r, c) not in visited
            )

        def dfs(r: int, c: int) -> int:
            if not is_move(r, c):
                return 0

            visited.add((r, c))
            area = 1
            for dr, dc in ((1,0), (0,1), (-1,0), (0,-1)):
                area += dfs(r + dr, c + dc)
            return area

        response = 0
        for r in range(rows):
            for c in range(cols):
                if is_move(r, c):   # start a new island
                    response = max(response, dfs(r, c))

        return response
