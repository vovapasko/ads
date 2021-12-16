# You are a professional robber planning to rob houses along
#  a street. Each house has a certain amount of money stashed,
#  the only constraint stopping you from robbing each of them
# is that adjacent houses have security systems connected and
# it will automatically contact the police if two adjacent houses
#  were broken into on the same night.

# Given an integer array nums representing the amount of money
# of each house, return the maximum amount of money you can rob
# tonight without alerting the police.
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * (len(nums) + 1)
        for i in range(1, len(dp) - 1):
            dp[i] = max(dp[i-1], nums[i-1], dp[i + 1])
        return dp[-1]


s = Solution()
print(s.rob([1, 2]))
print(s.rob([3, 10, 0]))
