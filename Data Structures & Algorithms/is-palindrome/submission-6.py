class Solution:
    def isPalindrome(self, s: str) -> bool:
        check = [ch.lower() for ch in s if ch.isalnum()]


        L =0 
        R = len(check)-1

        while L<R:
            if check[L]!=check[R]:
               return False
            L+=1
            R-=1

        return True 
