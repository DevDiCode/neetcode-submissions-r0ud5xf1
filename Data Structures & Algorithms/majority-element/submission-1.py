class Solution:
    def majorityElement(self, nums: List[int]) -> int:


        prev = 0 
        count = 0 


        for val in nums:
            if count==0 :

                prev = val
                count+=1
            

            else:
                if val == prev:
                    count+=1
                else:
                    count-=1
        
        return prev