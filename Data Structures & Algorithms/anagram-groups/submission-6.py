class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        
        lookup = defaultdict(list)



        for word in strs:

            word_hash = [0]*26

            for letter in word:
                word_hash[ord(letter)-ord("a")]+=1
            

            lookup[tuple(word_hash)].append(word)
        

        return list(lookup.values())
            