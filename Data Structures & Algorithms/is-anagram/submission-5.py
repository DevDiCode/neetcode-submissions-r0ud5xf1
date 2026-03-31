"""

Explore:
-> can there be an empty string :
-> can caps be ignore ?


BrainSotrm:
-> Using two Hasmpas
    Space = 0(n) +  O(n)
    Time = O(n) + O(N)

--> Using ASCII sum
    Space = o(1)
    Time =  0(n)

"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:


        if len(s) != len(t):
            return False


        result = [0]*26


        for val in s:

            result[ord(val) - ord("a")] +=1


        for char in t:

            if result[ord(char) - ord("a")] ==0 :
                return False
            result[ord(char) - ord("a")] -=1



        return True



from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:


        return Counter(s)==Counter(t)