class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        num_dict = defaultdict(int)
        for num in nums:
            num_dict[num] += 1
        
        total_count = 0

        for num in num_dict:
            count = num_dict[num]
            if count >= 2:
                total_count += count * (count -1) // 2
            
        return total_count
