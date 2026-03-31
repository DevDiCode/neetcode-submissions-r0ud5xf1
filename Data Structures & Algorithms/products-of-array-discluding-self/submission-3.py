# ✅ Problem: Product of Array Except Self
# 📚 Pattern: Prefix and Postfix Multiplication (Two-pass solution)
# 🎯 Goal: Return an array such that each element at index i is the product of all elements in the array except nums[i]

# ------------------------------------------------------------------------------
# 🔍 Step 1: Explore
# Given nums = [1, 2, 3, 4], the output should be [24, 12, 8, 6]
# Without using division and in O(n) time.

# ------------------------------------------------------------------------------
# 💡 Step 2: Brainstorm
# - Build prefix product array (product of elements before index i)
# - Multiply by postfix product (product of elements after index i)
# - Do this in two passes using only constant extra space (excluding result array)

# ------------------------------------------------------------------------------
# 🧭 Step 3: Plan
# 1. Create a response array initialized to 1
# 2. First pass: left ➝ right to build prefix product
# 3. Second pass: right ➝ left to build postfix product and multiply in-place

# ------------------------------------------------------------------------------
# 🧑‍💻 Step 4: Implement
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        response = [1] * n

        prefix = 1
        for i in range(n):
            response[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(n - 1, -1, -1):
            response[i] *= postfix
            postfix *= nums[i]

        return response

# ------------------------------------------------------------------------------
# ✅ Step 5: Verify
# Example:
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

# ------------------------------------------------------------------------------
# 🧪 Step 6: Demo
sol = Solution()
print(sol.productExceptSelf([1, 2, 3, 4]))  # Output: [24, 12, 8, 6]
