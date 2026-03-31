class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lookup = set()

        L = 0 
        count =0
        for R in range(len(s)):

            while s[R] in lookup:
                lookup.remove(s[L])
                L+=1
            

            lookup.add(s[R])
            count = max(count,R-L+1)
            
        
        return count
            
