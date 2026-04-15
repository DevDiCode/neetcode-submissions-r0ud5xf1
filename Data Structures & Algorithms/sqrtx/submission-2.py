class Solution:
    def mySqrt(self, x: int) -> int:
    

        if x==0 or x==1:
            return x
        

        def is_condition(mid):
            return mid*mid>x
        

        L = 0 
        R = x

        while L<R:

            mid = (L+R)//2

            if is_condition(mid):
                R=mid
            else:
                L = mid+1
        
        return L-1