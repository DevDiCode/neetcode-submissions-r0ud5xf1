class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        if not heights or not heights[0]:
            return []
        rows = len(heights)
        cols = len(heights[0])

        lookup_pacific = set()
        lookup_atlantic = set()


        #pacific tarversal 


        def is_move(r,c,lookup):

            return r in range(rows) and c in range(cols) \
                and (r,c) not in lookup

        

        def dfs(r,c,lookup):
            lookup.add((r,c))


            directions = [(0,1),(1,0),(-1,0),(0,-1)]

            for dr, dc in directions:
                new_row , new_col = r+dr , c+dc

                if not is_move(new_row,new_col,lookup):
                    continue

                curr_height = heights[r][c]
                neighbor_height = heights[new_row][new_col]

                if is_move(new_row,new_col,lookup) and neighbor_height>=curr_height:
                        dfs(new_row,new_col,lookup)
                


        # traverse pacific

        for col in range(cols):
            dfs(0,col,lookup_pacific)

        for row in range(rows):
            dfs(row,0 ,lookup_pacific)


        # traverse  atlamtic 

        for row in range(rows):
            dfs(row,cols-1,lookup_atlantic)

        for col in range(cols):
            dfs(rows-1,col,lookup_atlantic)


        result = [[r, c] for (r, c) in lookup_pacific & lookup_atlantic]

        return result        















        






