"""
1 2 ,3 4  5 6 7 8  k = 4

4 3 2 1 5 6 7 8 

4 3 2 1 8 7 6 5 




"""

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """


        if k<=0:
            return nums
        
        n = len(nums)
        k = k%n

        def swap(L,R):

            while L<R:

                nums[L], nums[R] = nums[R], nums[L]
                L+=1
                R-=1

        swap(0,n-1)
        swap(0,k-1)
        swap(k,n-1)