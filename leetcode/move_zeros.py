from typing import List


def moveZeroes(nums: List[int]) -> None:
    if len(nums) == 1:
        return
    for i in range(len(nums) - 1):
        if nums[i] == 0:
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
