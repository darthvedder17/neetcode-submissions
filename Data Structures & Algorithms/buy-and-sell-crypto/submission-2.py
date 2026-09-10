class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        cp = prices[0]
        for i in range(1,len(prices)):
            diff = prices[i] - cp
            if diff < 0:
                cp = prices[i]
            maxProfit = max(maxProfit, diff)
        return maxProfit
         
        