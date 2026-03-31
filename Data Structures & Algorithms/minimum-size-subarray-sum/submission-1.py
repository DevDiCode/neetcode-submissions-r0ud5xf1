# ------------------------------
# ✅ ENGINEERING METHOD TEMPLATE
# ------------------------------

# 1. Explore:
#    - Input:
#         • target: int → target sum
#         • nums: List[int] → array of positive integers
#    - Output:
#         • Smallest length of subarray with sum ≥ target
#    - Constraints:
#         • Subarray must be **contiguous**
#         • Return 0 if no such subarray exists

# 2. Brainstorm:
#    - Use dynamic sliding window
#    - Expand right pointer `R`, maintain running sum
#    - Shrink window from left as long as sum ≥ target
#    - Track the smallest valid window size

# 3. Plan:
#    - Initialize pointers L = 0 and sum = 0
#    - For each R in nums:
#         • Add nums[R] to sum
#         • While sum ≥ target:
#               ▸ Update result with min window size
#               ▸ Shrink from left by subtracting nums[L]
#    - If no valid window found → return 0

# 4. Implement:
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L = 0
        current_sum = 0
        min_len = float("inf")

        for R in range(len(nums)):
            current_sum += nums[R]

            while current_sum >= target:
                min_len = min(min_len, R - L + 1)
                current_sum -= nums[L]
                L += 1

        return 0 if min_len == float("inf") else min_len

# 5. Verify:
#    Input: target = 7, nums = [2,3,1,2,4,3] → Output: 2 (subarray [4,3])
#    Input: target = 4, nums = [1,4,4] → Output: 1
#    Input: target = 11, nums = [1,1,1,1,1,1,1,1] → Output: 0

# 6. Edge Cases:
#    - No subarray ≥ target → return 0
#    - All elements smaller than target
#    - Entire array is the smallest valid subarray

# ------------------------------
# ⏱ TIME COMPLEXITY: O(n)
#    - Each element is visited at most twice (once by R, once by L)
#
# 🧠 SPACE COMPLEXITY: O(1)
#    - Only constant space used for pointers and sum
# ------------------------------
