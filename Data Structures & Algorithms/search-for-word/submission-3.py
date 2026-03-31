class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        check = list(word)

        rows = len(board)
        cols = len(board[0])

        lookup = set()

        def is_move(r,c,index):
            return 0<=r<rows and 0<=c<cols and board[r][c]==check[index] 
    
        def helper(r,c, index):
            
            if index==len(check)-1 and board[r][c]==check[-1]:
                return True
            
            directions = [(1,0),(0,1),(-1,0),(0,-1)]

            temp = board[r][c]
            board[r][c] = None
            for dr , dc in directions:
                new_row = r+dr
                new_col = c+dc

                if is_move(new_row,new_col,index+1):
                    if helper(new_row,new_col,index+1):
                        return True
            board[r][c] = temp
            return False

            return False
        

        for r in range(rows):
            for c in range(cols):

                if board[r][c]==check[0]:   
                    if helper(r,c,0):
                        return True

        return False
            


        
       