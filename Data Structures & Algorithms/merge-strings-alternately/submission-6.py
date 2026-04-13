class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        response = []


        pointer1 = 0 

        pointer2 = 0 


        while pointer1<len(word1) and pointer2<len(word2):
            response.append(word1[pointer1])
            response.append(word2[pointer2])
            pointer1+=1
            pointer2+=1
        

        if pointer1<len(word1):
            response.extend(word1[pointer1:])
        
        if pointer2<len(word2):
            response.extend(word2[pointer2:])
        
        return "".join(response)

        