
"""

"""
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:


        pos = 0 

        for index , ele in enumerate(nums):

            if ele!=val:
                nums[pos]=ele
                pos+=1
        
        return pos
    