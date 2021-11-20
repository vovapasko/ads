# Given an integer array nums, find the contiguous subarray 
# (containing at least one number)
# which has the largest sum and return its sum.
# A subarray is a contiguous part of an array.
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sums = self.maxSum(nums, [], {})
        return max(max_sums)
        
    def maxSum(self, nums: list, sums: list, memo: dict) -> list:
        if len(nums) == 1: 
            sums.append(nums[0])
            return sums
        s = self.helper(nums, memo)
        sums.append(s)
        return self.maxSum(nums[1:], sums)
    
    def helper(self, arr):
        tmp = 0
        new_arr = []
        for el in arr:
            tmp += el
            new_arr.append(tmp)
        return max(new_arr)

s = Solution()
print(s.maxSubArray([-2, 3, 4, 5])) 
print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))