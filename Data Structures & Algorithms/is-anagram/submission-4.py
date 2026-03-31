class Solution:
    def isAnagram(self, s: str, t: str) -> bool:



        lookup  = [0]*26

        if len(s)!=len(t):
            return False

        for index, val  in enumerate(s):

            lookup[ord(s[index])-ord("a")]+=1
            lookup[ord(t[index])-ord("a")]-=1
        


        for val in lookup:
            if val!=0:
                return False
        

        return True
