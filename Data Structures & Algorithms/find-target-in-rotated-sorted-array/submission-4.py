class Solution:
    def search(self, nums: List[int], target: int) -> int:

        L = 0 
        R = len(nums)-1

        if not nums:
            return -1

        def is_condition(mid):

            same_side = (nums[mid] >= nums[0])  ==  (target >= nums[0])

            if same_side:
                return nums[mid]>=target

            else:
                return target>=nums[0]

        while L<R:

            mid = (L+R)//2

            if is_condition(mid):
                R=mid
            else:
                L=mid+1
        
        return L if nums[L] == target else -1


        