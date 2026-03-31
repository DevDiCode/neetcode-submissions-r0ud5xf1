class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        rows = len(matrix)
        cols = len(matrix[0])
        n = rows*cols-1


        L = 0 
        R = n

        def is_condition(index):
            row = index//cols
            col = index%cols

            return matrix[row][col]>=target

        while L<R:

            mid = (L+R)//2

            if is_condition(mid):
                R = mid
            
            else:
                L = mid+1
        
        result_row = L //cols
        result_col = L%cols

        return matrix[result_row][result_col]==target





        