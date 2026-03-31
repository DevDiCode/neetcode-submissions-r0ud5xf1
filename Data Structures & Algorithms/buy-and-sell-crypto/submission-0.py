class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        L = 0 

        if not prices or len(prices)<2:
            return 0 


        max_profit = float("-inf")
        for R in range(1, len(prices)):

            if prices[R]> prices[L]:

                max_profit = max(prices[R]- prices[L], max_profit)
            

            else:
                L = R
        

        return max_profit if  max_profit != float("-inf")  else 0
        