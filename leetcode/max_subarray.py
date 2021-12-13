# Given an integer array nums, find the contiguous subarray
# (containing at least one number)
# which has the largest sum and return its sum.
# A subarray is a contiguous part of an array.
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sums = []
        tmp_sum = 0
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                sums.append(tmp_sum)
                tmp_sum = 0
                continue
            else:
                tmp_sum += nums[i]
        return max(sums)


s = Solution()
print(s.maxSubArray([-2, 3, 4, 5]))
print(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
