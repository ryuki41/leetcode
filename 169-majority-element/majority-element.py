class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority_count = len(nums) / 2

        num_count = defaultdict(int)

        for num in nums:
            num_count[num] += 1
            if num_count[num] > majority_count:
                return num
