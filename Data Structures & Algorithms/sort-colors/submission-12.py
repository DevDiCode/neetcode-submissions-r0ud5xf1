class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low = 0 
        mid = 0 
        high= len(nums)-1

        
        def swap(L, R):

            nums[L], nums[R] = nums[R], nums[L]

        
        while mid<=high:

            if nums[mid]==0:
                swap(mid,low)
                mid+=1
                low+=1
            
            elif nums[mid]==1:
                mid+=1
            
            else:
                swap(mid,high)
                high-=1
