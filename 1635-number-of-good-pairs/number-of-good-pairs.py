class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        pairs_count = 0
        for i in range(len(nums)):
            # 自分自身はカウントしない
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    pairs_count += 1


        return pairs_count         