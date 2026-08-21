class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        num_count = defaultdict(int)

        for num in arr:
            num_count[num] += 1
        
        return len(num_count.values()) == len(set(num_count.values()))