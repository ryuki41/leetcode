class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        min_n = min(len(word1), len(word2))

        res = ""
        for i in range(min_n):
            res += word1[i] + word2[i]
        
        res += word1[min_n:]
        res += word2[min_n:]
        
        return res
