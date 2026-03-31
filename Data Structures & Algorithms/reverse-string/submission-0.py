class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        def swap(l,r):
            s[l], s[r] = s[r] , s[l]

        
        L =0 
        R = len(s)-1
        while L<=R:

            swap(L,R)
            L+=1
            R-=1
        
        
