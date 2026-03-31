from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [-1] * len(cost)

        def helper(index):
            if index == 0:
                return cost[0]
            if index == 1:
                return cost[1]
            if dp[index] != -1:
                return dp[index]

            dp[index] = cost[index] + min(helper(index - 1), helper(index - 2))
            return dp[index]

        return min(helper(len(cost) - 1), helper(len(cost) - 2))
