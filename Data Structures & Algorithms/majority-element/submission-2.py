class Solution:
    def majorityElement(self, nums: List[int]) -> int:


        if not nums:
            return -1

        candidate = 0
        count = 0

        for val in nums:

            if count == 0 or val==candidate :
                candidate = val
                count+=1
            
            else:
                count-=1
        
        return candidate

        