class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[-1 for _ in range(n+1)] for _ in range(n)]

        def helper(i, prev_index):
            if i == n:
                return 0

            if dp[i][prev_index + 1] != -1:
                return dp[i][prev_index + 1]

            not_pick = helper(i + 1, prev_index)
            pick = 0
            if prev_index == -1 or nums[i] > nums[prev_index]:
                pick = 1 + helper(i + 1, i)

            dp[i][prev_index + 1] = max(pick, not_pick)
            return dp[i][prev_index + 1]

        return helper(0, -1)
