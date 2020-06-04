class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        return sum(cost[0 if idx < len(costs)//2 else 1] for idx, cost in enumerate(sorted(costs, key=lambda c: c[0]-c[1])))
