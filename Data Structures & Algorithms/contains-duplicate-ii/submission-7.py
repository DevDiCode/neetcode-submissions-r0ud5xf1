class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()  # or set(), dict(), deque(), sum, etc.
        left = 0 


        for right in range(len(nums)):

            if nums[right] in window:
                return True
            

            window.add(nums[right])


            if right-left+1>k:
                window.remove(nums[left])
                left+=1
        

        return False
        

