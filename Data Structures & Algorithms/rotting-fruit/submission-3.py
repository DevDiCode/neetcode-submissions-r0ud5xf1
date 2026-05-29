class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:


        rows = len(grid)
        cols = len(grid[0])

        q = collections.deque()

        fresh_fruits = 0 

                # If there are no fresh oranges, zero time

        for r in range(rows):
            for c in range(cols):

                if grid[r][c]==2:
                    q.append((r,c))
                
                elif grid[r][c]==1:
                    fresh_fruits+=1
        
        if fresh_fruits == 0:
            return 0

        # BFS level-by-level; each level corresponds to one minute
        minutes = 0
        directions = ((1,0), (-1,0), (0,1), (0,-1))

        def is_move(r,c):
            return r in range(rows) and c in range(cols) and grid[r][c]==1

        while q :
            

            layer_size = len(q)

            for _ in range(layer_size):

                r , c = q.popleft()


                for dr, dc in directions:

                    new_row , new_col = r+dr, c+dc

                    if is_move(new_row,new_col):
                        grid[new_row][new_col]=2
                        fresh_fruits-=1
                        q.append((new_row,new_col))

            if q:
                minutes+=1

        return minutes if fresh_fruits==0 else -1

                    


                    




        


