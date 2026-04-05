class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:


        s1_lookup = Counter(s1)

        k = len(s1)
        n = len(s2)

        s2_lookup = Counter(s2[0:k]) 
        

        if s1_lookup == s2_lookup:
            return True
        

        for right in range(k,n):

            left = right-k
            s2_lookup[s2[right]]+=1
            s2_lookup[s2[left]]-=1


            if s2_lookup == s1_lookup:
                return True
        
        return False