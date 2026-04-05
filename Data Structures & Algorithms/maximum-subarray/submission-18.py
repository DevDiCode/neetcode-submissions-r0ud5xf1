class Solution:
    def maxSubArray(self, nums: List[int]) -> int:


        max_sum = -sys.maxsize-1

        csum = 0 

        for index,val in enumerate(nums):
            csum = csum+val

            csum = max(csum,val)
            max_sum = max(max_sum, csum)
        

        return max_sum
        





        