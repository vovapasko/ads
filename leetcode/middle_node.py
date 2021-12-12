# Given the head of a singly linked list,
# return the middle node of the linked list.
# If there are two middle nodes, return the second middle node.
from typing import Optional
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes_amount = self.count_nodes(head)
        middle = int(nodes_amount / 2)
        middle_node = self.get_ith_node(head, middle)
        return middle_node

    def count_nodes(self, head: ListNode) -> int:
        node = head
        counter = 1
        while node.next is not None:
            tmp = node.next
            counter += 1
            node = tmp
        return counter

    def get_ith_node(self, head: ListNode, i) -> ListNode:
        node = head
        counter = 0
        while counter != i:
            tmp = node.next
            counter += 1
            node = tmp
        return node
