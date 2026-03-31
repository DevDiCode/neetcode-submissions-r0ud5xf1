class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        max_sum = float("-inf")
        curr_sum = 0


        for val in nums:
            curr_sum = max(curr_sum+val , val)

            max_sum = max(curr_sum, max_sum)

        return max_sum
