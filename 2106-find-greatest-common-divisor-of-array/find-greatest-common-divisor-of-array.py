class Solution:
    def findGCD(self, nums: List[int]) -> int:
        a = max(nums)
        b = min(nums)

        def gcd(a: int, b: int):
            if a < b:
                a, b = b, a
            
            r = a % b

            if r == 0:
                return b
            else:
                return gcd(b, r)
        

        return gcd(a, b)