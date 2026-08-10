class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # 累積和を計算
        prefix_sum = [0] * (n+1)
        for i in range(n):
            prefix_sum[i+1] = nums[i] + prefix_sum[i]
        
        res = []

        for i in range(n):
            # 自身を除いた左側と右側の部分配列の合計
            left_sum = prefix_sum[i]
            right_sum = prefix_sum[n] - prefix_sum[i+1]
            left_cnt = i
            right_cnt = n - i - 1

            # 左側と右側の絶対値の差の合計
            left_total = nums[i] * left_cnt - left_sum
            right_total = right_sum - nums[i] * right_cnt

            res.append(left_total + right_total)
        
        return res