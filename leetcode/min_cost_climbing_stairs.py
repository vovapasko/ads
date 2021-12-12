# You are given an integer array cost where cost[i] is the cost of ith step on a
# staircase. Once you pay the cost, you can either climb one or two steps.
# You can either start from the step with index 0, or the step with index 1.
# Return the minimum cost to reach the top of the floor.

from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int], sum=0) -> int:
        if len(cost) == 2:
            sum += min(cost)
            return sum
        return self.minCostClimbingStairs(cost[:-1])
