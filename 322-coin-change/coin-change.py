class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        min_coins = [amount+1] * (amount+1)
        min_coins[0] = 0

        for i in range(1, amount+1):
            for c in coins:
                if i-c >= 0:
                    min_coins[i] = min(min_coins[i], min_coins[i-c]+1)
        
        if min_coins[amount] != amount+1:
            return min_coins[amount]
        else:
            return -1