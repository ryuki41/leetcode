class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        cnts = defaultdict(int)
        pairs = 0

        for num in nums:
            cnts[num] += 1


        for cnt in cnts.values():
            pairs += cnt * (cnt-1) // 2
        
        return pairs


