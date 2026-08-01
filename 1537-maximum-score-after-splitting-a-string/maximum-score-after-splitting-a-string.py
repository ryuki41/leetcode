class Solution:
    def maxScore(self, s: str) -> int:
        max_sum = 0

        for i in range(1, len(s)):
            num_sum = 0

            # leftの0の個数カウント
            for j in range(i):
                if s[j] == "0":
                    num_sum += 1

            # rightの1の個数カウント 
            for k in range(i, len(s)):
                if s[k] == "1":
                    num_sum += 1

            max_sum = max(max_sum, num_sum)
        
        return max_sum
