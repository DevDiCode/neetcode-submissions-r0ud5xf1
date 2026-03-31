class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        lookup = set()

        left = 0 
        response = 0 

        for right in range(len(s)):



            while s[right] in lookup:
                lookup.remove(s[left])
                left+=1
            
            lookup.add(s[right])
            response = max(right-left+1,response)
        
        return response