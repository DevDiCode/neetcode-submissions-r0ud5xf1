class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
    

       
        N  = len(coins)
        dp = [[0 for _ in range(amount + 1)] for _ in range(N)]

        # Initializing base condition
        for i in range(amount + 1):
            if i % coins[0] == 0:
                dp[0][i] = 1
            ''' Else condition is automatically fulfilled,
            as dp array is initialized to zero '''

        for ind in range(1, N):
            for target in range(amount + 1):
                notTaken = dp[ind - 1][target]

                taken = 0
                if coins[ind] <= target:
                    taken = dp[ind][target - coins[ind]]

                dp[ind][target] = (notTaken + taken)

        # Return the result
        return dp[N - 1][amount]