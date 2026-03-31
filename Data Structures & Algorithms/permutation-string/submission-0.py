from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        lookup = Counter(s1)

        L = 0 

        curr_lookup = {}

        for R in range(len(s2)):
            


            if R-L+1>len(s1):
                curr_lookup[s2[L]]-=1
                if curr_lookup[s2[L]]==0:
                    del curr_lookup[s2[L]]
                L+=1
            

            curr_lookup[s2[R]] = curr_lookup.get(s2[R],0)+1

            if R-L+1 == len(s1) and lookup==curr_lookup:
                return True
        
        return False






        