class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        nums.sort()

        max_sequence_count = 1
        cur_sequence_count = 1

        for i in range(1, len(nums)):
            # 同じ数字はカウントしないためスキップ
            if nums[i] == nums[i-1]:
                continue

            if nums[i] - nums[i-1] == 1:
                cur_sequence_count += 1
            else:
                max_sequence_count = max(max_sequence_count, cur_sequence_count)
                cur_sequence_count = 1
        
        return max(max_sequence_count, cur_sequence_count)





            

