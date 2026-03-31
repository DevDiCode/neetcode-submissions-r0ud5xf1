"""
Question 4 Concatenation of ARrays
"""

# Problem: Concatenation of Array
# https://leetcode.com/problems/concatenation-of-array/

# 🧠 Pattern: Array Manipulation + Index Wrapping
# No fancy data structures — just classic index control.

# ------------------------------
# ✅ Step 1: Explore
# ------------------------------
# Input: nums = [1, 2, 3]
# Output: [1, 2, 3, 1, 2, 3]
# Goal: Create a new array of size 2n with nums followed by nums

# ------------------------------
# ✅ Step 2: Brainstorm
# ------------------------------
# Brute Force:
# return nums + nums → valid in Python

# Manual Build (language-agnostic):
# Create new array of size 2 * n
# For i in range(2 * n), fill res[i] = nums[i % n]

# ------------------------------
# ✅ Step 3: Plan
# ------------------------------
# Use modulo to wrap around nums during second half of the array
# Allocate result array before filling

# ------------------------------
# ✅ Step 4: Implementation
# ------------------------------
from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * (2 * n)
        for i in range(2 * n):
            res[i] = nums[i % n]
        return res

# ------------------------------
# ✅ Step 5: Verify
# ------------------------------
# Test cases:
# [1,2,1] → [1,2,1,1,2,1]
# [5] → [5,5]
# [] → []

# Time Complexity: O(n)
# Space Complexity: O(n)

# ------------------------------
# ✅ Step 6: Reflect
# ------------------------------
# Pattern: Index Modulo / Array Doubling
# Insight: Use i % n to cycle through the original array
