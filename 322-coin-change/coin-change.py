class Solution:

  def coinChange(self, coins: list[int], amount: int) -> int:
    min_coins = [amount + 1] * (amount + 1)
    min_coins[0] = 0

    for i in range(1, amount+1):
        for c in coins:
            if i - c >= 0:
                min_coins[i] = min(min_coins[i], 1 + min_coins[i-c])
        
    if min_coins[-1] != amount+1:
        return min_coins[-1]
    else:
        return -1