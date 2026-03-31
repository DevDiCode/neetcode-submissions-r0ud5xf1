class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:


        lookup = defaultdict()
        if not nums:
            return [-1,-1]
        
        for key , val in enumerate(nums):

            if target - val in lookup :
                return [lookup[target-val],key]

            
            lookup[val]=key
        

        