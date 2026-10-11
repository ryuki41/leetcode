class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        strk = 1
        prev = 0
        res_count = 0

        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                strk += 1
            else:
                prev = strk
                strk = 1

            if prev >= strk:
                res_count += 1
        
        return res_count

        