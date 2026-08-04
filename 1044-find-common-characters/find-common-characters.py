class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        num_of_letters = 26
        min_letter_counter = [0] * num_of_letters

        for w in words[0]:
            min_letter_counter[ord(w) - ord("a")] += 1
        
        for i in range(1, len(words)):
            letter_counter = [0] * num_of_letters
            for w in words[i]:
                letter_counter[ord(w) -ord("a")] += 1
            
            for j in range(num_of_letters):
                min_letter_counter[j] = min(min_letter_counter[j], letter_counter[j])
        
        dup_counter = []
        for k in range(num_of_letters):
            for i in range(min_letter_counter[k]):
                dup_counter.append(chr(k + ord("a")))

        return dup_counter



        

        