class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        

        if not s:
            return True
        
        L  = 0 
        R = len(s)-1


        while L<R:

            s[L], s[R] = s[R], s[L]
            L+=1
            R-=1
        