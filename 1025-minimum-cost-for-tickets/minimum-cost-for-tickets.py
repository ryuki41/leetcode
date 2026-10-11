class Solution:
    def mincostTickets(self, days: list[int], costs: list[int]) -> int:
        min_cost = {}
        min_cost[0] = 0
        max_day = days[-1]
        days_set = set(days)

        for day in range(1, max_day+1):
            if not day in days_set:
                min_cost[day] = min_cost[day-1]
                continue

            day_cost = min_cost[day-1] + costs[0]
            week_cost = min_cost[max(day-7, 0)] + costs[1]
            month_cost = min_cost[max(day-30, 0)] + costs[2]

            min_cost[day] = min(day_cost, week_cost, month_cost)
        
        return min_cost[max_day]