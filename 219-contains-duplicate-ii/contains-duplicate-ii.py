class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        num_hash = {}

        for i in range(len(nums)):
            if nums[i] in num_hash and i - num_hash[nums[i]] <= k:
                return True

            num_hash[nums[i]] = i
        
        return False