class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # Sliding window
        ptr1 = 0
        maxProfit = 0
        
        for i in range(1, len(prices)):
            profit = prices[i] - prices[ptr1]
            if profit <= 0:
                ptr1 = i
            else:
                if profit > maxProfit:
                    maxProfit = profit
        
        return maxProfit
            