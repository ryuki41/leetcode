class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        apper_nums = {}

        for num in nums:
            if num in apper_nums:
                return True
            apper_nums[num] = 1
        
        return False
        