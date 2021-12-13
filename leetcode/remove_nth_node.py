# Given the head of a linked list, remove the nth node
# from the end of the list and return its head.
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        list_len = self.countList(head)
        delete_node_index = list_len - n
        return self.removeNthElement(head, delete_node_index, n)

    def countList(self, head: ListNode) -> int:
        node = head
        counter = 1
        while node.next is not None:
            tmp = node.next
            node = tmp
            counter += 1
        return counter

    def removeNthElement(self, head: ListNode, delete_node_index: int, n: int) -> ListNode:
        if delete_node_index == 0:
            if head.next is not None:
                tmp = head.next
                head = tmp
                return head
            return None
        node = head
        for _ in range(delete_node_index - 1):
            tmp = node.next
            node = tmp
        if n == 1:
            node.next = None
            return head
        tmp = node.next.next
        node.next = tmp
        return head
