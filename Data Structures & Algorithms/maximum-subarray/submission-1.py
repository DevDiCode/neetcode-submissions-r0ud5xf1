class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        max_sum = float("-inf")

        csum = 0 
        for i, val in enumerate(nums):

            csum+=val

            if csum>max_sum:
                max_sum = max(csum,max_sum)
            

            if csum<0:
                csum = 0 
        

        return max_sum
            

        