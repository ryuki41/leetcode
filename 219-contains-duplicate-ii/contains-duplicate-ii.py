class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        num_dic = defaultdict(int)

        for i in range(len(nums)):
            if nums[i] in num_dic and i - num_dic[nums[i]] <= k:
                return True

            num_dic[nums[i]] = i
        
        return False