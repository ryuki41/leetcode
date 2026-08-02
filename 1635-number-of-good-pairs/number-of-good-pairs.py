class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        duplicate_list = defaultdict(int)

        duplicate_count = 0
        for num in nums:
            duplicate_list[num] += 1
        
        for _, value in duplicate_list.items():


            if value > 1:
                duplicate_count += math.factorial(value) // (math.factorial(2) * math.factorial(value-2))
            
        return duplicate_count
        
        