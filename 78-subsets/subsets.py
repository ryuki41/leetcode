from copy import deepcopy as cp

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)

        res = []

        subset = []

        def rec(i):
            if i == N:
                res.append(cp(subset))
                return
            
            subset.append(nums[i])
            rec(i+1)

            subset.pop()
            rec(i+1)

            return

        rec(0)
        return res