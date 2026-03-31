class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        

        lookup = set()

        L = 0 

        for R in range(len(nums)):


            if R-L>k:
                lookup.remove(nums[L])
                L+=1
            

            if nums[R] in lookup:
                return True

            lookup.add(nums[R])
        
        return False

