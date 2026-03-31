# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:



        L=1
        R=n

        

        while L<R:

            mid = (L+R)//2


            if guess(mid)==-1:
                R = mid
            
            elif guess(mid)==1:
                L = mid+1
            
            else:
                return mid
        

        return L


            

        

        