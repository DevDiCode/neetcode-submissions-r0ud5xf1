class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
                
        if not nums:
            return []

        n = len(nums)
        
        res = [None]*2 * n


        for i,val in enumerate(nums):
            res[i] = res[i+n] = val
        
        return res