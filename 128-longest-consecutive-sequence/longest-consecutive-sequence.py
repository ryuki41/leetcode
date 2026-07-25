class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort()

        max_sequence_count = 0

        sequence_count = 0
        while len(nums) > 0:
            sequence_count = 1
            current_num = nums.pop(0)

            for i in range(len(nums)):
                if nums[0] - current_num == 1:
                    current_num = nums.pop(0)
                    sequence_count += 1
                else: 
                    max_sequence_count = max(max_sequence_count, sequence_count)
                    break
        
        return max(max_sequence_count, sequence_count)





            

