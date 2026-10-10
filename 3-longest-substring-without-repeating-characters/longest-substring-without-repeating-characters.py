class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        max_len = 0
        cur_len = 0

        for i, char in enumerate(s):
            if char in seen:
                max_len = max(max_len, cur_len)
                cur_len = 0
                seen = set()
                for j in reversed(range(i)):
                    if s[j] == char:
                        break
                    seen.add(s[j])
                    cur_len += 1
                
            seen.add(char)
            cur_len += 1
        
        return max(max_len, cur_len)



