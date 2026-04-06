class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        left = 0 


        response = 0 
        max_freq = 0
        lookup = defaultdict(int)
        response = 0 

        def is_valid(right):
            if (right-left+1)-max_freq>k:
                return False

            return True

        for right in range(len(s)):


            lookup[s[right]]+=1

            max_freq = max(max_freq, lookup[s[right]])


            while not is_valid(right):

                lookup[s[left]]-=1

                if lookup[s[left]]==0:
                    del lookup[s[left]]
                
                left+=1
            
            response = max(right-left+1,response)
        

        return response


            




        