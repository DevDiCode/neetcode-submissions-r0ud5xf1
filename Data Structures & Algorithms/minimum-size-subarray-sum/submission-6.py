class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:


        L = 0 
        curr_sum = 0 

        min_len = float("inf")


        for R in range(len(nums)):
            
            curr_sum+=nums[R]

            while curr_sum>=target:

                min_len = min(min_len,R-L+1)
                curr_sum-=nums[L]
                L+=1
        

        return min_len if min_len!= float("inf") else 0


        