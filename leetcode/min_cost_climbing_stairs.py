# You are given an integer array cost where cost[i] is the cost of ith step on a
# staircase. Once you pay the cost, you can either climb one or two steps.
# You can either start from the step with index 0, or the step with index 1.
# Return the minimum cost to reach the top of the floor.

from typing import List


class Solution:

    ## time: O(N)
    ## Space: O(N)
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * (len(cost))
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, len(cost)):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])
        return min(dp[-2], dp[-1])
    ## time: O(N)
    ## space: O(1)

    def minCost2(self, cost: List[int]) -> int:
        a = cost[0]
        b = cost[1]
        for i in range(2, len(cost)):
            tmp = cost[i] + min(b, a)
            a = b
            b = tmp
        return min(a, b)


s = Solution()
print(s.minCostClimbingStairs([3, 2, 4]))
