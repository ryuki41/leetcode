class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_pointer = 0

        if len(s) == 0:
            return  True

        for t_pointer in range(len(t)):
            if s[s_pointer] == t[t_pointer]:
                s_pointer += 1
                if s_pointer == len(s):
                    # sの全ての文字の並び順が担保されている
                    return True

        return False