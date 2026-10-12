class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        min_coin = [amount+1] *(amount+1)
        min_coin[0] = 0

        for i in range(1, amount+1):
            for c in coins:
                if i-c >= 0:
                    min_coin[i] = min(min_coin[i], min_coin[i-c]+1)
        
        if min_coin[amount] == amount+1:
            return -1
        else:
            return min_coin[amount]

