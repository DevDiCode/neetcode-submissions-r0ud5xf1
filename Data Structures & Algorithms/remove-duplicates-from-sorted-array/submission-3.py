# ✅ PROBLEM: Remove Duplicates from Sorted Array (LeetCode 26)
# 💡 PATTERN: Two Pointer (In-place overwrite)
# 🎯 GOAL: Modify the array in-place to remove duplicates from a sorted array. Return the new length.

# ------------------------------
# ENGINEERING METHOD
# ------------------------------

# 1. Explore:
#    - Input: Sorted integer array (e.g., [1,1,2,3,3,4])
#    - Output: Length of unique elements and in-place modified array (e.g., [1,2,3,4,...])
#    - Key Constraint: Must modify in-place with O(1) space

# 2. Brainstorm:
#    - Since the array is sorted, all duplicates are adjacent.
#    - We can maintain a `write pointer` to overwrite duplicates.

# 3. Plan:
#    - Initialize `L = 1` (next unique write position)
#    - Traverse with `R = 1 to n-1`
#    - If `nums[R] != nums[R-1]`, write it to `nums[L]`, then increment `L`
#    - Return `L` as the count of unique elements

# 4. Implement:

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # L points to the next unique position
        L = 1

        for R in range(1, len(nums)):
            if nums[R] != nums[R - 1]:
                nums[L] = nums[R]
                L += 1

        return L

# 5. Verify:
#    Input: [1,1,2,3,3,4] ➝ Output: 4, Array becomes [1,2,3,4,...]
#    Input: [1] ➝ Output: 1
#    Input: [] ➝ Output: 0

# 6. Edge Cases:
#    - Empty array → return 0
#    - All duplicates (e.g., [2,2,2,2]) → return 1
#    - All unique → no overwrites, return len(nums)

# ------------------------------
# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(1)
# ------------------------------
