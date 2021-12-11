from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        non_zeroes = []
        for el in nums:
            if el != 0:
                non_zeroes.append(el)
        for i in range(len(non_zeroes)):
            nums[i] = non_zeroes[i]
        for i in range(len(non_zeroes), len(nums)):
            nums[i] = 0
