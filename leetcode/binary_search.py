from typing import List
import math


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        right = len(nums) - 1
        left = 0

        while True:
            center = math.ceil((right + left) / 2)
            if nums[center] == target:
                return center
            if center >= right:
                break
            if nums[center] > target:
                right = center
            else:
                left = center

        return -1


s = Solution()
s.search([-1, 0, 3, 5, 9, 12], target=9)
s.search([-1, 0, 3, 5, 9, 12], target=2)
s.search([5], target=5)
s.search([5], target=2)
s.search([2, 5], target=5)
