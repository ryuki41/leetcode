class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n1 = len(word1)
        n2 = len(word2)

        res = []
        for i in range(min(n1, n2)):
            res.append(word1[i])
            res.append(word2[i])
        
        if n1 > n2:
            for j in range(n2, n1):
                res.append(word1[j])
        elif n1 < n2: 
            for k in range(n1, n2):
                res.append(word2[k])

        return "".join(res)
