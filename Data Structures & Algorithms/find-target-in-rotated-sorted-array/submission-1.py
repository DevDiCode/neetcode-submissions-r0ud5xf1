# ------------------------------------------------------
# ✅ Problem: Search in Rotated Sorted Array
#         (LeetCode 33: https://leetcode.com/problems/search-in-rotated-sorted-array/)
# ------------------------------------------------------
# Given a rotated sorted array nums and an integer target, return its index if found,
# otherwise return -1. The array contains distinct integers and is rotated at an unknown pivot.
#
# Key Examples to Master:
# Example 1: nums = [4,5,6,7,0,1,2], target = 0  -> Output: 4
# Example 2: nums = [4,5,6,7,0,1,2], target = 3  -> Output: -1
# Example 3: nums = [1],               target = 0  -> Output: -1
# ------------------------------------------------------

# 1) Explore:
#    - Input: rotated sorted array (strictly increasing before rotation), target int
#    - Output: index of target or -1
#    - Constraints: O(log n) time, unique values (no duplicates)

# 2) Brainstorm:
#    - Engineering method with a predicate for lower-bound style search:
#      We define a virtual sorted order using nums[0] as a reference:
#      • If nums[mid] and target are on the same side relative to nums[0],
#        compare nums[mid] to target directly.
#      • Otherwise, decide based on which side target lies on.
#    - Use binary search with while left < right and shrink toward the first index
#      where predicate becomes True, then verify equality.

# 3) Plan:
#    - If nums is empty -> return -1
#    - Define predicate(mid):
#         same_side = (nums[mid] >= nums[0]) == (target >= nums[0])
#         if same_side: return nums[mid] >= target
#         else:         return target >= nums[0]
#    - Do lower-bound search on [0, n-1] using while left < right:
#         if predicate(mid): right = mid
#         else:              left  = mid + 1
#    - After loop, check nums[left] == target ? left : -1

class Solution:
    def search(self, nums, target):
        if not nums:
            return -1

        def predicate(mid):
            # Determine if mid is at or beyond the lower-bound position
            same_side = (nums[mid] >= nums[0]) == (target >= nums[0])
            if same_side:
                # Both on same side: direct comparison in that side's order
                return nums[mid] >= target
            else:
                # Different sides: if target is on the "left" (>= nums[0]), we should move left
                return target >= nums[0]

        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if predicate(mid):
                right = mid
            else:
                left = mid + 1

        return left if nums[left] == target else -1

# 4) Verify:
# sol = Solution()
# print(sol.search([4,5,6,7,0,1,2], 0))   # 4
# print(sol.search([4,5,6,7,0,1,2], 3))   # -1
# print(sol.search([1], 0))               # -1
# print(sol.search([6,7,0,1,2,4,5], 6))   # 0
# print(sol.search([6,7,0,1,2,4,5], 5))   # 6
# print(sol.search([1,3], 3))             # 1
# print(sol.search([3,1], 3))             # 0

# 5) Edge Cases:
#    - Empty array -> -1
#    - Single element: return 0 if equal else -1
#    - Target equals nums[0]
#    - Target on either side of pivot

# 6) Complexity:
#    - Time: O(log n)
#    - Space: O(1)

# ------------------------------------------------------
# Pattern Recap (Engineering Method):
#   - Define search space: indices [0, n-1]
#   - Build a monotonic predicate in a "virtual sorted" view using nums[0]
#   - Apply lower-bound binary search and verify at the end
# ------------------------------------------------------
