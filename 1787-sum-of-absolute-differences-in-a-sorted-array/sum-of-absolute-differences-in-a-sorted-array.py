class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # i番目より左側にある絶対差の合計
        left_abs = [0] * n
        for i in range(1, n):
            left_abs[i] = left_abs[i-1] + (nums[i] - nums[i-1]) * i

        # i番目より右側にある絶対差の合計
        right_abs = [0] * n
        for i in reversed(range(n-1)):
            right_abs[i] = right_abs[i+1] + (nums[i+1] - nums[i]) * (n-1-i)
        
        # i番目の左側と右側の絶対差の合計
        res = []
        for i in range(n):
            res.append(left_abs[i] + right_abs[i])

        return res


