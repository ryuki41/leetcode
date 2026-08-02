class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return []

        sum_nums = []
        sum_nums.append(nums[0])

        for i in range(1, len(nums)):
            sum_nums.append(nums[i]+sum_nums[i-1])
        
        return sum_nums
