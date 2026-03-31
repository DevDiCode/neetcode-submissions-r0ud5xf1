class Solution:
    def search(self, nums: List[int], target: int) -> int:

        
        def condition(mid):
            # Decide if the value at mid is >= target in virtual sorted array space
            if (nums[mid] >= nums[0]) == (target >= nums[0]):
                return nums[mid] >= target
            else:
                # If mid and target are on opposite sides
                return target >= nums[0]

        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if condition(mid):
                right = mid
            else:
                left = mid + 1

        return left if nums[left] == target else -1
