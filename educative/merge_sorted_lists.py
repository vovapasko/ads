
class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        self.arbitrary = None


def insert_at_head(head, data):
    newNode = LinkedListNode(data)
    newNode.next = head
    return newNode


def create_linked_list(lst):
    list_head = None
    for x in reversed(lst):
        list_head = insert_at_head(list_head, x)
    return list_head


def merge_two_lists(list1: LinkedListNode, list2: LinkedListNode) -> LinkedListNode:
    root = LinkedListNode(-1)
    tmp = root
    while list1 is not None and list2 is not None:
        if list1.data <= list2.data:
            tmp.next = LinkedListNode(list1.data)
            list1 = list1.next
        else:
            tmp.next = LinkedListNode(list2.data)
            list2 = list2.next
        tmp = tmp.next
    tmp.next = list1 or list2
    return root.next


def mergeKLists(lists):
    # write your code here
    if len(lists) == 1:
        return lists[0]
    results = lists[0]
    for i in range(len(lists) - 1):
        results = merge_two_lists(results, lists[i + 1])
    return results


def display(head):
    temp = head
    while temp:
        print(str(temp.data), end="")
        temp = temp.next
        if temp != None:
            print(", ", end="")


# Driver code
a = create_linked_list([11, 41, 51])
b = create_linked_list([21, 23, 42])
c = create_linked_list([25, 56, 66, 72])

print("All movie ID's from best to worse are:")
display(mergeKLists([a, b, c]))
