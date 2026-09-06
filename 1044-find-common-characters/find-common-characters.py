class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        num_of_letters = 26
        min_freq = [0] * num_of_letters

        for w in words[0]:
            min_freq[ord(w) - ord("a")] += 1
        
        for i in range(1, len(words)):
            word = words[i]
            freq = [0] * num_of_letters

            for w in word:
                freq[ord(w) - ord("a")] += 1
            
            for i in range(num_of_letters):
                min_freq[i] = min(min_freq[i], freq[i])

        res = []
        for i, num in enumerate(min_freq):
            for _ in range(num):
                res.append(chr(i + ord("a")))

        return res