class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        # my answer
        # for idx, cost in enumerate(costs):
        #     costs[idx].append(cost[0]-cost[1])
        # costs = sorted(costs, key=lambda x : x[-1])
        # return sum(cost[0] if idx + 1 <= len(costs)//2 else cost[1] for idx, cost in enumerate(costs))
 
        sm=sum([i for i,j in costs])
        diff=sorted([j-i for i,j in costs])
        return sm+sum(diff[:len(costs)//2])