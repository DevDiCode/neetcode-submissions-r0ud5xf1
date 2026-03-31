class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        

        L = 0 
        zero_count = 0 
        response = 0 


        for R in range(len(nums)):

            if nums[R]==0 :
                zero_count+=1

            


            while zero_count>k:
                
                if nums[L]==0:
                    zero_count-=1
                
                L+=1
            
            response = max(response, R-L+1)
        
        return response