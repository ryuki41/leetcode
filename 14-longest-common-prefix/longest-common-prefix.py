class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        min_length = 200
        for st in strs:
            if len(st) < min_length:
                min_length = len(st)
        
        strs.sort()

        common_str = ""
        for i in range(min_length):
            if strs[0][i] != strs[-1][i]:
                return common_str
            common_str += strs[0][i]

        return common_str
