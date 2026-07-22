class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_dict = defaultdict(int)
        
        for i in range(len(nums)):
            num_dict[nums[i]] += 1
            if num_dict[nums[i]] == 2:
                return True

        return False





