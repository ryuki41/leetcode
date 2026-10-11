class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        max_vowels = 0
        vowels = ["a", "e", "i", "o", "u"]
        vowels = set(vowels)
        print(vowels)
        for i in range(k):
            if s[i] in vowels:
                max_vowels += 1
        
        cur_vowels = max_vowels
        for right in range(k, len(s)):
            left = right - k

            if s[left] in vowels:
                cur_vowels -= 1
            if s[right] in vowels:
                cur_vowels += 1

            max_vowels = max(max_vowels, cur_vowels)
        
        return max_vowels

        