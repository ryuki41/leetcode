class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        current_max_sum = 0
        for i in range(k):
            current_max_sum += nums[i]
        
        max_sum = current_max_sum

        # 累計の最大値を取得しておいて最後に最大の平均値を返す
        for i in range(k,len(nums)):
            current_max_sum += nums[i]
            current_max_sum -= nums[i-k]
            max_sum = max(max_sum, current_max_sum)
        
        return max_sum / k
