class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_len = 0
        seen = set()

        for char in s:
            while char in seen:
                seen.remove(s[left])
                left += 1
            seen.add(char)
            max_len = max(max_len, len(seen))

        return max_len