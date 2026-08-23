class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_list = {}

        for num in nums:
            if num in num_list:
                return True
            num_list[num] = True
        
        return False
