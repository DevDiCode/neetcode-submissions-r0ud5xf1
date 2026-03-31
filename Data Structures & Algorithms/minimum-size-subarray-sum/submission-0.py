
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L = 0 

        response = float("inf")

        curr_sum = 0 
        for R in range(len(nums)):
            curr_sum+=nums[R]
            
            while curr_sum>=target:


                response = min(response,R-L+1)
                curr_sum-=nums[L]
                L+=1

            
        
        return  0 if response ==float("inf") else response
        