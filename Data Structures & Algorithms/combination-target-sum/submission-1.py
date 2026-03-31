# Combination Sum (LeetCode 39) — Pick / Not-Pick Approach
# --------------------------------------------------------
# Given distinct integers candidates and a target, return all unique combinations
# where candidates can be chosen unlimited times and sum to target. Order does not matter.

from typing import List

# 1) Exploration:
# - Each candidate can be picked any number of times (including 0).
# - Combinations are order-insensitive (treat [2,3] same as [3,2]), so we control order via index.
# - Distinct candidates => no dedup by value required.

# 2) Brainstorm:
# A) Pick / Not-Pick (chosen)
#    - At index i, we have two choices:
#       1) Pick candidates[i]: stay at i (unlimited use), reduce remaining target
#       2) Not-pick candidates[i]: move to i+1 (try next candidate)
#    - Base cases:
#       - If target == 0: record the path
#       - If target < 0 or i == n: stop
#
# B) For-loop + start index (alternative)
#    - Iterate i from start..n-1, try value, recurse with same i; backtrack.
#    - Equivalent in effect; different structure.

# 3) Plan:
# - helper(i, remaining, path):
#     - If remaining == 0: res.append(copy of path); return
#     - If remaining < 0 or i == n: return
#     - Pick: path.append(candidates[i]); helper(i, remaining - candidates[i]); path.pop()
#     - Not-pick: helper(i + 1, remaining, path)

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res: List[List[int]] = []
        path: List[int] = []
        n = len(candidates)

        # Optional: sort for nicer output and minor pruning in other variants
        candidates.sort()

        def helper(i: int, remaining: int) -> None:
            if remaining == 0:
                res.append(path.copy())
                return
            if remaining < 0 or i == n:
                return

            # 1) Pick candidates[i] (stay at i because we can reuse it)
            path.append(candidates[i])
            helper(i, remaining - candidates[i])
            path.pop()

            # 2) Not-pick candidates[i] (move to next index)
            helper(i + 1, remaining)

        helper(0, target)
        return res

# 4) Edge Cases:
# - target = 0 -> [[]]
# - No valid combination -> []
# - Single candidate equal to target -> [[target]]
# - Large target with small candidate -> deeper recursion; pick/not-pick naturally handles it

# 5) Complexity:
# - Time: Exponential in the size of the solution space (worst-case), common for combination enumeration
# - Space: O(target/min(candidates)) recursion depth for the pick chain; plus output size

# 6) Tests (commented):
# print(Solution().combinationSum([2,3,6,7], 7))  # [[2,2,3], [7]]
# print(Solution().combinationSum([2,3,5], 8))   # [[2,2,2,2],[2,3,3],[3,5]]
# print(Solution().combinationSum([1], 1))       # []
# print(Solution().combinationSum([2], 2))       # [[1,1]]
