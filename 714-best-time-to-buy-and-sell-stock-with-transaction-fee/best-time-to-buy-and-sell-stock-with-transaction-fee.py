class Solution:
    def maxProfit(self, prices: list[int], fee: int) -> int:
        if not prices:
            return 0
            
        # 1日目の初期状態
        cash = 0               # 株を持っていない状態の利益
        hold = -prices[0]      # 株を買った状態の利益（手持ちから株価を支払う）
        
        # 2日目以降（インデックス1から最後まで）ループを回す
        for price in prices[1:]:
            # 一時的に前日の値を保持するか、同時に更新する
            new_cash = max(cash, hold + price - fee)
            new_hold = max(hold, cash - price)
            
            cash = new_cash
            hold = new_hold
            
        # 最終的に株を持っていない状態（cash）の利益が最大になっている
        return cash