class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        
        def gcd(len1: int, len2: int):
            r = len1 % len2

            if r == 0:
                return len2
            else:
                return gcd(len2, r)
        
        return str1[:gcd(len(str1), len(str2))]