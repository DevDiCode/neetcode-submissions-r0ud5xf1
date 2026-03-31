class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start =0 
        mid = 0 
        last = len(nums)-1  




        def swap(l,r):
            nums[l] , nums[r] = nums[r], nums[l]
        while mid<=last:
            if nums[mid]==0:
                swap(start,mid)
                start+=1
                mid+=1
            elif nums[mid]==1:
                mid+=1
            else:
                swap(mid,last)
                last-=1
        return nums