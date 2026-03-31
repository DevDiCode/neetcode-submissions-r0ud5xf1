class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        L = 0 

        lookup = {}

        response = 0 

        for R in range(len(s)):

            lookup[s[R]] = lookup.get(s[R],0)+1

            while len(lookup)>2:
                lookup[s[L]]-=1

                if lookup[s[L]]==0:
                    del lookup[s[L]]
                
                L+=1
            
            response = max(R-L+1,response)
        

        return response




