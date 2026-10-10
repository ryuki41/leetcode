class Solution:
    def climbStairs(self, n: int) -> int:
        step_count = {}
        step_count[0] = 1
        step_count[1] = 1

        if n < 2:
            return step_count[n]

        for i in range(2, n+1):
            step_count[i] = step_count[i-2] + step_count[i-1]
        
        return step_count[n]