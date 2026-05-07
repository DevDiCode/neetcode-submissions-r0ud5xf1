class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []


        def helper(index, curr):             # Helper function
            if index == len(nums):           # Base case
                result.append(curr.copy())   # MUST copy!
                return
            
            curr.append(nums[index])         # PICK
            helper(index + 1, curr)
            curr.pop()                       # BACKTRACK
            
            helper(index + 1, curr)          # NOT PICK
        
        helper(0, [])
        return result