# Given a sorted array of distinct integers and a target value, return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.
# You must write an algorithm with O(log n) runtime complexity.
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        right = len(nums) - 1
        left = 0
        m = 0
        while left <= right:
            m = int((right + left) / 2)
            if nums[m] == target:
                return m
            if nums[m] > target:
                right = m - 1
            else:
                left = m + 1
        # further means our element is not in searched array and we have to
        # find it possible index
        if target > nums[right]:
            return right + 1
        if target < nums[left]:
            return left
        return m


s = Solution()
s.searchInsert([1, 3, 5, 6], 5)
