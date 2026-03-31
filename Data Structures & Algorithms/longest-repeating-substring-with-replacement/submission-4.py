class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        lookup ={}

        L = 0 


        max_freq = 0 
        response = 0 

        for R in range(len(s)):
            lookup[s[R]] = lookup.get(s[R],0)+1
            max_freq = max(max_freq,lookup[s[R]])


            if R-L+1 - max_freq >k :

                lookup[s[L]]-=1
                L+=1
            
            response = max(R-L+1, response)
        
        return response
