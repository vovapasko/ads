from typing import List
# solved! Use Modulo ariphmetic


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n_map = {}
        for i in range(len(nums)):
            new_index = (i + k) % len(nums)
            n_map[new_index] = nums[i]
        for key, value in n_map.items():
            nums[key] = value
