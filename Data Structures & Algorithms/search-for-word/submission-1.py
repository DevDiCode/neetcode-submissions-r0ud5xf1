class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        check = list(word)
        rows = len(board)
        cols = len(board[0])
        lookup = set()

        def is_move(r, c, index):
            return 0 <= r < rows and 0 <= c < cols and board[r][c] == check[index] and (r, c) not in lookup
        
        def helper(r, c, index):
            # If we've reached the end of the word
            if index == len(check) - 1 and board[r][c] == check[-1]:
                return True
            
            # Mark the current cell as visited
            lookup.add((r, c))
            
            directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            for dr, dc in directions:
                new_row = r + dr
                new_col = c + dc
                
                if is_move(new_row, new_col, index + 1):
                    if helper(new_row, new_col, index + 1):
                        return True

            # Backtrack by removing the current cell from visited set
            lookup.remove((r, c))
            return False
        
        # Check each cell in the board
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == check[0]:
                    if helper(r, c, 0):
                        return True
        
        return False
