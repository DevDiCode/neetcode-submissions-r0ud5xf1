class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0 


        response = 0
        L = 0 
        for R in range(1,len(prices)):
            if  prices[R]>prices[L]:
                response = max(response,  prices[R]-prices[L])
            
            else:
                L = R
        
        return response 

        