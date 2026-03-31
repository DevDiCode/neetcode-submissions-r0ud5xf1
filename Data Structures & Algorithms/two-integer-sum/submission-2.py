class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}


        for index,val in enumerate(nums):

            if target-val in lookup:
                return [lookup[target-val],index]
            else:
                lookup[val] = index

        
        return -1

            
        