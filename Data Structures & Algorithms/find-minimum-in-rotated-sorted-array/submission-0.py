class Solution:
    def findMin(self, nums: List[int]) -> int:

        if not nums:
            return -1

        
        def is_condition(mid):
            return nums[mid]<nums[-1]


        L = 0
        R = len(nums) - 1

        if nums[L] < nums[R]:
            return nums[0]


        while L<R:


            mid = (L+R)//2

            if is_condition(mid):
                R = mid
            
            else:
                L = mid+1
        
        return nums[L]
        