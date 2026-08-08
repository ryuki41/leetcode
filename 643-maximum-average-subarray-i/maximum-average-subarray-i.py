class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        current_max_num = 0
        max_num = 0
        for i in range(k):
            current_max_num += nums[i]
            max_num += nums[i]

        # 累計の最大値を取得しておいて最後に最大の平均値を返す
        for i in range(k,len(nums)):
            current_max_num += nums[i]
            current_max_num -= nums[i-k]
            max_num = max(max_num, current_max_num)
        
        return max_num / k
