class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_cnt = defaultdict(int)

        for num in nums:
            num_cnt[num] += 1
            if num_cnt[num] >= 2:
                return True

        return False        
        