class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        

        pos1 = 0 
        pos2 = 0 

        res = ""
        respos  = 0 

        while pos1<len(word1) and pos2<len(word2):

            if respos ==0 or respos%2==0:
                res+=(word1[pos1])
                respos+=1
                pos1+=1

            else:
                res+=word2[pos2]
                respos+=1
                pos2+=1


        while pos1<len(word1):
            res+=word1[pos1]
            pos1+=1
        
        while  pos2<len(word2):
            res+=word2[pos2]
            pos2+=1


        return res

        