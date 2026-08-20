class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        prefix_sum = []
        prefix_sum.append(0)

        for i in range(len(gain)):
            prefix_sum.append(prefix_sum[-1] + gain[i])
        
        return max(prefix_sum)