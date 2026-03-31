class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        pos=0 
        for i , curr in enumerate(nums):

            if curr!=val:
                nums[pos]=curr
                pos+=1
            
        
        return pos