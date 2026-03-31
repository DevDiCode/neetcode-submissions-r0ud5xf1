# ------------------------------------------------------
# ✅ Problem: Binary Search
#         (LeetCode 704: https://leetcode.com/problems/binary-search/)
# ------------------------------------------------------

# 1. Explore:
#    - Input: Sorted integer list 'nums', integer 'target'
#    - Output: Index of 'target' if present in nums; else -1
#    - Constraints: O(log n) time, unique elements, ascending order

# 2. Brainstorm:
#    - Standard binary search fits: halve range each time.
#    - Can use custom predicate for "first index where nums[idx] >= target"
#    - After loop, check if found exactly

# 3. Plan:
#    - Define L = 0, R = len(nums)-1 (search the whole index space)
#    - While L < R: compute mid
#        - If nums[mid] >= target, shrink right (R = mid)
#        - Otherwise, advance left (L = mid+1)
#    - After exiting loop, check if nums[L] == target (may not–if not, return -1)

# 4. Implement:
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def isTrue(index):
            return nums[index] >= target
        
        L = 0
        R = len(nums) - 1
        
        while L < R:
            mid = (L + R) // 2
            if isTrue(mid):
                R = mid
            else:
                L = mid + 1
        
        return L if nums and nums[L] == target else -1

# 5. Verify:
sol = Solution()
print(sol.search([-1,0,3,5,9,12], 9))    # 4
print(sol.search([-1,0,3,5,9,12], 2))    # -1
print(sol.search([1], 1))                # 0
print(sol.search([], 1))                 # -1

# 6. Edge Cases:
#    - nums = []       => -1
#    - nums = [1], search=1 => 0
#    - nums = [1], search=2 => -1
#    - target at start or end of nums

# 7. Complexity:
#    - Time: O(log n)
#    - Space: O(1)

# ------------------------------------------------------
# Pattern Recap:
#   - Engineering binary search for leftmost value >= target (lower bound)
#   - Confirm match explicitly at end.
#   - Handles all edge cases by construction.
# ------------------------------------------------------
