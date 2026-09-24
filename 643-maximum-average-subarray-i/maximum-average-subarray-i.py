class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_num = 0
        for i in range(k):
            max_num += nums[i]    

        cur_num = max_num
        for j in range(k, len(nums)):
            cur_num -= nums[j-k]
            cur_num += nums[j]
            max_num = max(max_num, cur_num)

        return max_num / k
