class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        nums.sort()

        max_seq = 1
        cur_seq = 1
        for i in range(1, len(nums)):
            if nums[i-1] == nums[i]:
                continue
            
            if nums[i-1]+1 == nums[i]:
                cur_seq += 1
            else:
                max_seq = max(max_seq, cur_seq)
                cur_seq = 1
        
        return max(max_seq, cur_seq)

