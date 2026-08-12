class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        if n <= 1:
            return 0

        left_score = 1 if s[0] == "0" else 0
        right_score = 0
        for i in range(1,n):
            if s[i] == "1":
                right_score += 1
        
        max_total_score = left_score + right_score


        for i in range(1,n-1):
            if s[i] == "0":
                left_score += 1
            else:
                right_score -= 1
            
            max_total_score = max(max_total_score, left_score + right_score)
        
        return max_total_score