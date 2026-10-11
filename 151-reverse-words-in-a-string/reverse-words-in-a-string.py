class Solution:
    def reverseWords(self, s: str) -> str:
        res = []
        word_right = len(s) - 1
        word_right_exist = False

        for i in reversed(range(len(s))):
            if not word_right_exist and s[i] != " ":
                word_right_exist = True
                word_right = i
            
            if word_right_exist and s[i] == " ":
                word_right_exist = False
                res.append(s[i+1:word_right+1])
        
        if s[0] != " ":
            res.append(s[0:word_right+1])
        
        return " ".join(res)
