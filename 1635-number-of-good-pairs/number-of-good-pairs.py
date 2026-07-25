class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        groups = defaultdict(int)
        for num in nums:
            groups[num] += 1
        
        counter = 0
        for key, g in groups.items():

            if g == 1:
                continue
            # 組み合わせ分足す
            counter += g * (g-1) // 2

        return counter
