class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L = 0 

        response = float("-inf")


        R = len(heights)-1

        while L<R:

            area = (R-L) * min(heights[L],heights[R])

            response = max(area, response)

            if heights[R]> heights[L]:
                L+=1
            
            else:
                R-=1
        
        return response 

