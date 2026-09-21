class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy = prices[0]
        profit = 0

        for price in prices:
            if buy > price:
                buy = price
            elif profit < price - buy:
                profit = price - buy
            
        return profit
