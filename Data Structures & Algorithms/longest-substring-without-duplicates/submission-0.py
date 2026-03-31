class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        lookup = set()

        max_len = 0 
        L  = 0 


        for R in range(len(s)):

            
            while s[R] in lookup:

                lookup.remove(s[L])
                L+=1

            
            
            max_len = max(max_len, R-L+1)
            lookup.add(s[R])
        

        return max_len


        