class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        right_list = [0] * n
        left_list = [0] * n

        # i番目の時にiの左側の積を求める
        # iが0の時は左側には何もないので1とする
        left_list[0] = 1
        for i in range(1, n):
            left_list[i] = left_list[i-1] * nums[i-1]
        
        # i番目の時にiの右側の積を求める
        # iが一番右の時は右側に何もないので1とする
        right_list[-1] = 1
        for i in reversed(range(n-1)):
            right_list[i] = right_list[i+1] * nums[i+1]
        
        res = []

        for i in range(n):
            res.append(left_list[i] * right_list[i])

        return res  