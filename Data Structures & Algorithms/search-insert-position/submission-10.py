class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        

        if not nums:
            return -1



        def is_condition(index):
            return nums[index]>=target
        
        L = 0 
        R = len(nums)

        while L<R:

            mid  = (L+R)//2


            if is_condition(mid):
                R = mid
            
            else:
                L = mid+1
        
        return L

        


            