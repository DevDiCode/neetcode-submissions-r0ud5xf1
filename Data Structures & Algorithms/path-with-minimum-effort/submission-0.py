class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        effort_to = [[float('inf')] * cols for _ in range(rows)]
        effort_to[0][0] = 0

        minheap = [(0, 0, 0)]  # (effort, row, col)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while minheap:
            effort, r, c = heapq.heappop(minheap)
            # Early exit: we've reached destination with minimal effort
            if r == rows - 1 and c == cols - 1:
                return effort

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    step_effort = abs(heights[nr][nc] - heights[r][c])
                    new_effort = max(effort, step_effort)
                    if new_effort < effort_to[nr][nc]:
                        effort_to[nr][nc] = new_effort
                        heapq.heappush(minheap, (new_effort, nr, nc))

        # Fallback: in most cases, function already returns from early exit
        return effort_to[rows - 1][cols - 1]