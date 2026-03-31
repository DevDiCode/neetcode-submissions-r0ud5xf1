class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        nums.sort()
        for index, val in enumerate(nums):

            if index>0 and nums[index-1] == nums[index]:
                return True
        
        return False
