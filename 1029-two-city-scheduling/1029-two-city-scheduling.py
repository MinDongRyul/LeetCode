class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        for idx, cost in enumerate(costs):
            costs[idx].append(cost[0]-cost[1])
        costs = sorted(costs, key=lambda x : x[-1])
        return sum(cost[0] if idx + 1 <= len(costs)//2 else cost[1] for idx, cost in enumerate(costs))