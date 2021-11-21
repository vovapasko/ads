from typing import NoReturn, Union

class MyNode:
    def __init__(self, value) -> None:
        self.value = value
        self.next: MyNode = None
    

class MyLinkedList:
    def __init__(self, firs_el: MyNode = None) -> None:
        self.first: MyNode = firs_el

    def read(self, index: int) -> object: 
        current = self.__iterate_until(index)
        return current.value

    def insert(self, value: MyNode, index: Union[int, None] = None) -> None:
        # if index None -> insert to the end
        if index == 0:
            tmp = self.first
            value.next = tmp
            self.first = value
            return
        if index is not None:
            current: MyNode = self.__iterate_until(index - 1)
            tmp: MyNode = current.next
            value.next = tmp
        else:
            current: MyNode = self.__get_last()
        current.next = value
        
        
    def delete(self, index: int) -> object:
        # if index None -> delete from the end and return it's value
        if index == 0:
            tmp = self.first.next
            self.first = tmp
        if index > 0:
            current: MyNode = self.__iterate_until(index - 1)
            tmp = current.next.next
            removed_el = current.next
            current.next = tmp
            return removed_el

    def print(self) -> None:
        current = self.first
        while current.next is not None:
            print(str(current.value) + " -> ",end=" ")
            nxt = current.next
            current = nxt
        print(str(current.value))

    def __iterate_until(self, index) -> MyNode:
        assert index >= 0
        i = 0
        current: MyNode = self.first
        while i < index:
            next_el = current.next
            if next_el is None:
                raise IndexError()
            current = next_el
            i += 1
        return current

    def __get_last(self) -> MyNode:
        current: MyNode = self.first
        while current.next is not None:
            next_el = current.next
            current = next_el
        return current

n0 = MyNode(0)
n1 = MyNode(1)
n2 = MyNode(2)
n3 = MyNode(3)

ll = MyLinkedList(n0)
ll.insert(n1)
ll.insert(n2)
ll.insert(n3)
ll.print()

ll.delete(1)
ll.print()
ll.insert(MyNode(10), 1)
ll.print()
ll.delete(3) 
ll.print()
ll.insert(MyNode(-1), 0)
ll.print()