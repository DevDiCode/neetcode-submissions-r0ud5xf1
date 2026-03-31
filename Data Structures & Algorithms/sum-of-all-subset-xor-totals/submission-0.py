class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:

        def helper(index, curr):
            if index == len(nums):
                return curr
            # Include nums[index]
            take = helper(index + 1, curr ^ nums[index])
            # Exclude nums[index]
            skip = helper(index + 1, curr)
            return take + skip
        return helper(0, 0)