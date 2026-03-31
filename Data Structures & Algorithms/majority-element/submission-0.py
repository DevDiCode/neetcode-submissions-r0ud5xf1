class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        ele = None
        count = 0 


        for val in nums:

            if count ==0:
                ele = val
                count+=1
            
            elif val==ele:
                count+=1
            
            else:
                count-=1
        
        return ele
        