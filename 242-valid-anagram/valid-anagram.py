class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == 0 and len(t) == 0:
            return True

        if len(t) != len(s):
            return False

        s_word_count = defaultdict(int)
        t_word_count = defaultdict(int)

        for i in range(len(s)):
            s_word_count[s[i]] += 1
            t_word_count[t[i]] += 1
        
        return s_word_count == t_word_count