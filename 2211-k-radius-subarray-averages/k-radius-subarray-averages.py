class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return nums
        
        n = len(nums)

        ans = [-1 for _ in range(n)]

        if 2*k+1 > n:
            return ans
        
        total = 0
        for i in range(2*k+1):
            total += nums[i]
        
        for j in range(k, n-k):
            ans[j] = total // (2*k+1)

            if j+k+1 < n:
                total -= nums[j-k]
                total += nums[j+k+1]

        return ans
