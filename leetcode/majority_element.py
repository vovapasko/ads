# Given an array nums of size n, return the majority element.
#The majority element is the element that appears more than ⌊n / 2⌋ times.
#  You may assume that the majority element always exists in the array.
from typing import List
from math import floor
class Solution:
    def majorityElement(self,nums: List[int]) -> int:
        nums_map = {}
        for el in nums:
            if nums_map.get(el, None) is None:
                nums_map[el] = 1
            else:
                nums_map[el] += 1
        for el in nums:
            if nums_map[el] > self.get_delta(len(nums)):
                return el

    def get_delta(self,n):
        return floor(n / 2)