class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)

        if total_sum % 2 != 0:
            return False

        target = total_sum // 2
        n = len(nums)
        dp = [[-1 for _ in range(target + 1)] for _ in range(n)]  # DP table for memoization

        def helper(index, target):
            if target == 0:
                return True
            if index == 0:
                return nums[0] == target

            if dp[index][target] != -1:
                return dp[index][target]

            not_pick = helper(index - 1, target)
            pick = False
            if nums[index] <= target:
                pick = helper(index - 1, target - nums[index])

            dp[index][target] = pick or not_pick
            return dp[index][target]

        return helper(n - 1, target)
