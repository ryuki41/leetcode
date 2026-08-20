class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        right_sum = sum(nums) - nums[0]
        left_sum = 0

        for i in range(len(nums)):
            if left_sum == right_sum:
                return i
            
            if i < len(nums)-1:
                left_sum += nums[i]
                right_sum -= nums[i+1]
        
        return -1

        