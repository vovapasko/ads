# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order,
# find two numbers such that they add up to a specific target number.
# Let these two numbers be numbers[index1] and numbers[index2]
#  where 1 <= index1 < index2 <= numbers.length.
# Return the indices of the two numbers, index1 and index2, added by one as an integer
#  array[index1, index2] of length 2.
# The tests are generated such that there is exactly one solution.
#  You may not use the same element twice.
from typing import List

# working solution but o(n^2). For some cases too long
# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:
#         for i in range(len(numbers) - 1):
#             for j in range(i + 1, len(numbers)):
#                 if numbers[i] + numbers[j] == target:
#                     return [i+1, j+1]


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start, end = 0, len(numbers) - 1
        while start < end:
            if numbers[start] + numbers[end] == target:
                return[start + 1, end + 1]
            if numbers[start] + numbers[end] > target:
                end -= 1
            else:
                start += 1


s = Solution()
s.twoSum([2, 3, 4], 6)