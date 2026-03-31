# Pacific Atlantic Water Flow (LeetCode 417)
# 
# Engineering Method
# 
# Exploration
# Given a heights matrix where water flows from a cell to neighbors with height less than or equal to the current cell, 
# find all coordinates that can reach both the Pacific (top/left edges) and Atlantic (bottom/right edges) oceans. 
# Reverse the flow: start from each ocean’s borders and traverse “uphill” to neighbors with height greater than or equal to current. 
# The intersection of the two reachability sets yields all required cells.



# Brainstorm
# Perform two reverse flood-fills (DFS or BFS):
# - Pacific sources: all cells on row 0 and col 0
# - Atlantic sources: all cells on row m-1 and col n-1
# - Reverse transition rule: from (r, c) to (nr, nc) if heights[nr][nc] >= heights[r][c]
# Maintain two visited sets (per ocean) and return their intersection.
# 
# Plan
# - Guard empty matrix
# - Define dfs(r, c, seen): add (r, c) to seen; for each neighbor (nr, nc), 
#   if in-bounds, not seen, and heights[nr][nc] >= heights[r][c], recurse
# - Run dfs from all Pacific border cells into pacific; similarly for Atlantic into atlantic
# - Return list of [r, c] for cells in pacific ∩ atlantic

from typing import List, Set, Tuple

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        rows, cols = len(heights), len(heights[0])
        pacific: Set[Tuple[int, int]] = set()
        atlantic: Set[Tuple[int, int]] = set()

        def in_bounds(r: int, c: int) -> bool:
            return 0 <= r < rows and 0 <= c < cols

        def dfs(r: int, c: int, seen: Set[Tuple[int, int]]) -> None:
            if (r, c) in seen:
                return
            seen.add((r, c))
            for dr, dc in ((1,0), (0,1), (-1,0), (0,-1)):
                nr, nc = r + dr, c + dc
                # Reverse flow step: only move if neighbor is >= current height
                if in_bounds(nr, nc) and (nr, nc) not in seen and heights[nr][nc] >= heights[r][c]:
                    dfs(nr, nc, seen)

        # Pacific borders: top row and left column
        for c in range(cols):
            dfs(0, c, pacific)
        for r in range(rows):
            dfs(r, 0, pacific)

        # Atlantic borders: bottom row and right column
        for c in range(cols):
            dfs(rows - 1, c, atlantic)
        for r in range(rows):
            dfs(r, cols - 1, atlantic)

        # Intersection: cells reachable by both oceans
        return [[r, c] for (r, c) in pacific & atlantic]

# Edge Cases
# - Empty matrix -> []
# - Single row or single column -> many cells reach both; handled by border starts
# - Plateaus (equal heights) propagate reachability via >= rule
# - Non-rectangular inputs are out of scope (problem guarantees m x n)
#
# Time and Space Complexity
# - Time: O(m * n), since each cell is visited at most twice (once per ocean)
# - Space: O(m * n) for visited sets; recursion stack can reach O(m * n) in worst case (use BFS to avoid recursion limits)
