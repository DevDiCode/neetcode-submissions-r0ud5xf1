class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        lookup = set()

        left = 0 


        def is_valid(index):

            if s[index] in lookup:
                return False
            

            return True
        
        response = 0 
        for right in range(len(s)):


            while not is_valid(right):
                lookup.remove(s[left])
                left+=1
            
            lookup.add(s[right])

            response = max(right-left+1,response)
        
        return response