class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_pointer = 0

        if len(s) == 0:
            return True
            
        for i in range(len(t)):
            if t[i] == s[s_pointer]:
                s_pointer += 1
                if s_pointer == len(s):
                    return True
            
        return s_pointer == len(s)
            