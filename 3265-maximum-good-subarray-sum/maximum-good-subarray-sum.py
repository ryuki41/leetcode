class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # 累積和を計算する
        prefix_sum = [0] * (n+1)
        for i in range(n):
            prefix_sum[i+1] = prefix_sum[i] + nums[i]
        
        max_sum = -math.inf

        num_index = {}

        for i, num in enumerate(nums):
            for target in [num - k, num + k]:
                if target in num_index:
                    max_sum = max(max_sum, prefix_sum[i+1] - prefix_sum[num_index[target]])
                
                if num in num_index and prefix_sum[i+1] - prefix_sum[num_index[num]] < num:
                    num_index[num] = i
                
                elif num not in num_index:
                    num_index[num] = i
                
        return max_sum if max_sum != -math.inf else 0


        