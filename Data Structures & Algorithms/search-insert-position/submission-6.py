class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0 
        right = len(nums)



        def is_condition(mid):
            if nums[mid]>=target:
                return True
            
            return False
        


        while left<right:

            mid = (left+right)//2


            if is_condition(mid):
                right = mid
            else:
                left = mid+1
        
        return left 
            