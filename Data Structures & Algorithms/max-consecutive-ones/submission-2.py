class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        

        response = 0 
        curr = 0 

        for val in nums:
            if val==1:
                curr+=1
                response = max(curr,response)
            
            else:
                curr= 0 

        return response