class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        if k>len(nums):
            k = k%len(nums)

        def swap(L , R):

            while L<R:
                nums[L] , nums[R] = nums[R], nums[L]
                L+=1
                R-=1
        


        swap(0,len(nums)-1)
        swap(0,k-1)
        swap(k,len(nums)-1)


        return nums
