"""


"""


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        


        n = 2*len(nums)
        res = [None]*n



        for i in range(len(res)):

            
                res[i] = nums[i%len(nums)] if i>=len(nums) else nums[i]
        
        return res