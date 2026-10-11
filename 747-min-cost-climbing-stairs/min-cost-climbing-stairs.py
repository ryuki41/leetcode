class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        cost_num = {}
        cost_num[0] = 0
        cost_num[1] = 0

        for i in range(2, len(cost)+1):
            cost_num[i] = min(cost_num[i-2] + cost[i-2], cost_num[i-1] + cost[i-1])
        
        return cost_num[len(cost)]



        