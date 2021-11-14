from typing import List


def plusOne(digits: List[int]) -> List[int]:
    return foo(i=len(digits) - 1, nums=digits)


def foo(i, nums):
    if nums[i] == 9:
        nums[i] = 0
        if i == 0:
            return [1] + nums
        return foo(i - 1, nums)
    nums[i] += 1
    return nums
