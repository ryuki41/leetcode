class Solution:
    def maxScore(self, s: str) -> int:
        # rightになるscoreを数える
        right_score = 0
        for i in range(len(s)):
            if s[i] == "1":
                right_score += 1
        
        left_score = 0
        max_score = 0
        # 1つずつleftに移していきscoreをカウントする
        for i in range(len(s)-1):
            if s[i] == "0":
                left_score += 1
            else:
                right_score -= 1    
            score = left_score + right_score
            max_score = max(max_score, score)
        
        return max_score
            


