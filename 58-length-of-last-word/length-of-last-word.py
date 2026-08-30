class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        for i in reversed(range(len(s))):
            if s[i].isalpha():  
                length += 1
            if not s[i].isalpha() and length != 0:
                break

        return length