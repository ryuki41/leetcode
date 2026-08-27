class Solution:
    def romanToInt(self, s: str) -> int:
        symbol_val = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        sum_num = 0
        next_symbol_skip = False

        for i in range(len(s)):
            if next_symbol_skip:
                next_symbol_skip = False
                continue
            
            if i == len(s)-1:
                sum_num += symbol_val[s[i]]
                continue
                
            if s[i] == "I" and s[i+1] in ["V", "X"]:
                next_symbol_skip = True
                sum_num += symbol_val[s[i+1]] - 1
                continue

            if s[i] == "X" and s[i+1] in ["L", "C"]:
                next_symbol_skip = True
                sum_num += symbol_val[s[i+1]] - 10
                continue

            if s[i] == "C" and s[i+1] in ["D", "M"]:
                next_symbol_skip = True
                sum_num += symbol_val[s[i+1]] - 100
                continue
            
            sum_num += symbol_val[s[i]]
        
        return sum_num

        