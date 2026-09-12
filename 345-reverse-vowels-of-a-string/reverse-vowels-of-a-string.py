class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel = ["a", "e", "i", "o", "u"]

        n = len(s)
        left = 0
        right = n - 1

        s = list(s)
        while left < right:
            if not s[left].lower() in vowel:
                left += 1
                continue

            if not s[right].lower() in vowel:
                right -= 1
                continue

            s[left], s[right] = s[right], s[left]

            left += 1
            right -= 1
        
        return "".join(s)