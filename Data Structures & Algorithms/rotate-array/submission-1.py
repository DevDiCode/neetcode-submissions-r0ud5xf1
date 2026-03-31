class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        
        Explore:
        -> Input array 
        -> outpur array 
        -> rotte by K palces


        """
        n = len(nums)
               
        k %= n

        def helper(l,r):

            while l<r:
                nums[l], nums[r] = nums[r], nums[l]
                l+=1
                r-=1
        
        helper(len(nums)-k,n-1)
        print(nums)
        helper(0,n-k-1)
        print(nums)
        helper(0,n-1)
