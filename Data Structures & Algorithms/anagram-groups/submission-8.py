class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        response = defaultdict(list)


        for word in strs:
            
            hash = [0]*26
            for ch in word:

                hash[ord(ch)-ord("a")]+=1

            
            response[tuple(hash)].append(word)
        

        return list(response.values())

        
        