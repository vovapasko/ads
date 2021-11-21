from my_doubly_node import MyDoublyNode

class MyDoublyLinkedList:
    def __init__(self, first= None, last = None) -> None:
        self.first = first
        self.last = last

    def insert(self, node: MyDoublyNode) -> None:
        if self.first is None:
            self.first = node
            self.last = node
        else:
            self.first.next = self.last
            node.previous = self.last
            self.last.next = node