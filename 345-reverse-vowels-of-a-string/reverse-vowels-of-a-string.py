class Solution:
    def reverseVowels(self, s: str) -> str:
        left = 0
        right = len(s) -1

        reverse_vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

        s_list = list(s)

        while left < right:
            while left < right and not s_list[left] in reverse_vowels:
                left += 1
            
            while left < right and not s_list[right] in reverse_vowels:
                right -= 1
            
            if left < right:
                s_list[left], s_list[right] = s_list[right], s_list[left]
            
            left += 1
            right -= 1
        
        return "".join(s_list)