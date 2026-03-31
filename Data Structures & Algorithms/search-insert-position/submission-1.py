class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        

        L = 0 
        R = len(nums)



        def is_condition(mid):
            if nums[mid]>=target:
                return True
        
            return False
        

        while L<R:
            mid = (L+R)//2

            if is_condition(mid):
                R = mid
            
            else:
                L = mid+1
        
        return L 
        


