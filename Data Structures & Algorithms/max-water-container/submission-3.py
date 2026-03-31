class Solution:
    def maxArea(self, heights: List[int]) -> int:

        if not heights:
            return 0 
        

        max_area = 0


        L = 0 
        R = len(heights)-1

        while L<R:

            curr_area = min(heights[R], heights[L]) * (R-L)

            max_area = max(curr_area,max_area)

            if heights[L]<=heights[R]:
                L+=1
            else:
                R-=1
        
        return max_area
        