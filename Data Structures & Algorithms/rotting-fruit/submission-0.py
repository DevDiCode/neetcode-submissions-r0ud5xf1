from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        fresh_count = 0
        rows = len(grid)
        cols = len(grid[0])

        q = deque()

        # Initialize the queue with rotten oranges and count fresh oranges
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh_count += 1
                if grid[r][c] == 2:
                    q.append((r, c))

        # If no fresh oranges, return 0 immediately
        if fresh_count == 0:
            return 0

        # Initialize time count
        time_count = 0

        # Helper function to check valid moves
        def move(r, c):
            return 0 <= r < rows and 0 <= c < cols and grid[r][c] == 1

        # Perform BFS
        while q and fresh_count > 0:
            # Increment time after each round (level of BFS)
            time_count += 1

            for i in range(len(q)):  # Process all rotten oranges at the current time step
                r, c = q.popleft()

                directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

                for dr, dc in directions:
                    new_row = r + dr
                    new_col = c + dc

                    if move(new_row, new_col):
                        # Rot the fresh orange and add it to the queue
                        q.append((new_row, new_col))
                        grid[new_row][new_col] = 2
                        fresh_count -= 1

        # If there are still fresh oranges left, return -1, otherwise return the time
        return -1 if fresh_count > 0 else time_count
