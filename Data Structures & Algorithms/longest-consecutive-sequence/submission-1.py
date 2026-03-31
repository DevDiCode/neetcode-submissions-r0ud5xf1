class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        lookup = set(nums)

        streak = 0 
        response = 0 


        i = 0 
        for num in nums:

            if num-1 not in lookup:
                streak = 1
                while num+streak in lookup:
                    streak+=1
                
                response = max(streak,response)
        
        return response