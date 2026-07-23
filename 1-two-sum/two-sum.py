class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}
        
        for i, v in enumerate(nums):
            if target - v in hash_table:
                return [hash_table[target - v], i]
            
            hash_table[v] = i
