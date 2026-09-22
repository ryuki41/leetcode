class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_array = s.split(" ")
        if len(s_array) != len(pattern):
            return False

        s_set = set()

        pattern_map = {}
        for i in range(len(pattern)):
            c = pattern[i]
            if c in pattern_map:
                if pattern_map[c] != s_array[i]:
                    return False
            else:
                if s_array[i] in s_set:
                    return False

            pattern_map[c] = s_array[i]
            s_set.add(s_array[i])
            
        return True

