class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0

        for i in range(len(nums)):
            if nums[left] != nums[i]:
                nums[left+1] = nums[i]
                left += 1
        
        return left+1