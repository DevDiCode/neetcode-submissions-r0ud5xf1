class Solution:
    def maxArea(self, heights: List[int]) -> int:

        left = 0 
        right = len(heights)-1
    


        response = 0


        while left<right:
            min_height = min(heights[left], heights[right])
            distance = right - left
            response = max(response, min_height*distance)

            if heights[left]<heights[right]:
                left+=1
            
            else:
                right-=1
        


        return response

