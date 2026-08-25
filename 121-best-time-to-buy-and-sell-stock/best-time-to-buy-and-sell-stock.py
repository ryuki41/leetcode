class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = prices[0]
        profit = 0

        for i in range(1,len(prices)):
            p = prices[i]

            if buy_price > p:
                buy_price = p
            
            profit = max(profit, p - buy_price)
        
        return profit
