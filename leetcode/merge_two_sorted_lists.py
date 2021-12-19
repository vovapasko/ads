# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists in a one sorted list. The list should be made by splicing together
# the nodes of the first two lists.
# Return the head of the merged linked list.
from typing import Optional, Union

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = tmp = ListNode(0)
        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                tmp.next = list1
                list1 = list1.next
            else:
                tmp.next = list2
                list2 = list2.next
            tmp = tmp.next
        tmp = list1 or list2
        return head.next


s = Solution()
s.mergeTwoLists([1, 2, 4], [1, 3, 4])
print()
