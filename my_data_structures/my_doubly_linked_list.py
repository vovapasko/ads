from my_doubly_node import MyDoublyNode

class MyDoublyLinkedList:
    def __init__(self, first: MyDoublyNode) -> None:
        self.first = first
        self.last = first

    def insert(self, node: MyDoublyNode) -> None:
        if self.first == self.last:
            self.first.next = node
            self.last = node
            self.last.previous = self.first
        else:
            tmp = self.last
            tmp.next = node
            node.previous = tmp
            self.last = node 

    def delete(self, index: int):
        el_to_delete: MyDoublyNode = self.__iterate_until(index)
        prev = el_to_delete.previous
        nxt = el_to_delete.next
        prev.next = nxt
        nxt.previous = prev

    def __iterate_until(self, index):
        i = 0
        current: MyDoublyNode = self.first
        while i < index:
            next_el = current.next
            if next_el is None:
                raise IndexError()
            current = next_el
            i += 1
        return current

    def print(self):
        current = self.first
        while current.next is not None:
            print(str(current.value) + " -> ",end=" ")
            nxt = current.next
            current = nxt
        print(str(current.value))

    def print_reversed(self):
        current = self.last
        while current.previous is not None:
            print(str(current.value) + " <- ",end=" ")
            prev = current.previous
            current = prev
        print(str(current.value))
    
n0 = MyDoublyNode(0)
n1 = MyDoublyNode(1)
n2 = MyDoublyNode(2)
n3 = MyDoublyNode(3)
n4 = MyDoublyNode(4)

dl = MyDoublyLinkedList(n0)
dl.insert(n1)
dl.insert(n2)
dl.insert(n3)
dl.insert(n4)
dl.print()
dl.print_reversed()
dl.delete(3)
dl.print()
dl.print_reversed()
