class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [[float('inf')] * (amount + 1) for _ in range(len(coins))]

        # Base case: 0 amount can be made with 0 coins
        for i in range(len(coins)):
            dp[i][0] = 0

        # Fill the DP table
        for i in range(len(coins)):
            for j in range(1, amount + 1):
                # Option 1: Not pick the coin
                not_pick = dp[i - 1][j] if i > 0 else float('inf')

                # Option 2: Pick the coin if it's within the target
                pick = float('inf')
                if coins[i] <= j:
                    pick = 1 + dp[i][j - coins[i]]

                # Choose the minimum of picking or not picking the coin
                dp[i][j] = min(not_pick, pick)

        # Check final result in dp array
        result = dp[len(coins) - 1][amount]
        return result if result != float('inf') else -1
