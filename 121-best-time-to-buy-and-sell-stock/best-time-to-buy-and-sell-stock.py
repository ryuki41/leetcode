class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        # n日目以降の最高株価
        max_prices = [0] * n
        max_prices[n-1] = prices[n-1]

        for i in reversed(range(1, n-1)):
            max_prices[i] = max(prices[i], max_prices[i+1])
        
        max_profit = 0
        print(max_prices)
        for i in range(n-1):
            cur_max_profit = max_prices[i+1] - prices[i]
            max_profit = max(max_profit, cur_max_profit)
        
        return max_profit