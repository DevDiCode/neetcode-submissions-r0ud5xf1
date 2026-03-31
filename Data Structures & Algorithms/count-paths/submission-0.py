# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:



#         def is_move(r,c):

#             return 0<=r<m and 0<=c<n

        
#         def helper(r,c):

#             if r==0 and c==0:
#                 return 1
            

#             direction = [(-1,0),(0,-1)]

#             count= 0 
#             for dr, dc in direction:

#                 new_row = r+dr
#                 new_col = c+dc


#                 if is_move(new_row, new_col):
#                     count += helper(new_row, new_col)

            
#             return count
        

#         return helper(m - 1, n - 1)


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        dp = [[-1 for _ in range(n)] for _ in range(m)]


        def is_move(r,c):

            return 0<=r<m and 0<=c<n

        
        def helper(r,c):



            if dp[r][c]!=-1:
                return dp[r][c]

            if r==0 and c==0:
                return 1
    


            direction = [(-1,0),(0,-1)]

            count= 0 
            for dr, dc in direction:

                new_row = r+dr
                new_col = c+dc


                if is_move(new_row, new_col):
                    count += helper(new_row, new_col)

            
            return count
        

        return helper(m - 1, n - 1)

        