from typing import List


def intercept(nums1: List[int], nums2: List[int]) -> List[int]:
    if len(nums1) <= len(nums2):
        return helper(nums1, nums2)
    return helper(nums2, nums1)


def helper(small: list, big: list) -> list:
    repeated_list = []
    for i_el in small:
        for j_el in big:
            if i_el == j_el:
                repeated_list.append(i_el)
                break
    return repeated_list


intercept([1, 2], [1, 1])
