class Solution:
    def search(self, nums: List[int], target: int) -> int:
        

        def isTrue(index):
            return nums[index]>=target

    

        L = 0 
        R = len(nums)-1


        while L<R:
            mid = (L+R)//2

            if isTrue(mid):
                R= mid
            
            else:
                L = mid+1
        

        return L if nums[L]==target else -1