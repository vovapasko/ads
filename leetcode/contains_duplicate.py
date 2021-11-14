from typing import List


def containsDuplicate(self, nums: List[int]) -> bool:
    store = {}
    for num in nums:
        el = store.get(num, 0)
        if el == 0:
            store[num] = 1
        else:
            return True
    return False
