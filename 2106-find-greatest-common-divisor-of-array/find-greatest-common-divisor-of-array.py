class Solution:
    def findGCD(self, nums: List[int]) -> int:
        min_num = min(nums)
        max_num = max(nums)

        return gcd(max_num, min_num)
    
    def gcd(a, b):
        if a < b:
            a, b = b, a
        
        r = a % b
        if r == 0:
            return b
        
        return gcd(b, r)