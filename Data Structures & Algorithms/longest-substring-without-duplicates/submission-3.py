class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:


        lookup = set()


        response = 0 


        L = 0 


        for R in range(len(s)):


            while s[R] in lookup :

                lookup.remove(s[L])
                L+=1
            

            lookup.add(s[R])
            response = max(R-L+1 , response)

        return response


        