import sys
class Solution:
    def maxArea(self, heights: List[int]) -> int:


        left = 0
        right = len(heights) - 1

        res = float("-inf")
        while left < right:

            min_height = min(heights[left], heights[right])
            distance = right - left
            print(min_height, distance)
            res = max(res, min_height*distance)

            if heights[left] < heights[right]:
                left+=1

            else:
                right-=1


        return res
