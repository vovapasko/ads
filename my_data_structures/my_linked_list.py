from typing import Union

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
            
    def __iterate_until(self, index) -> MyNode:
        assert index >= 0
        i = 0
        current: MyNode = self.first
        while i < index:
            next_el = current.next
            if next_el is None:
                raise IndexError()
            current = next_el
        return current

    def __get_last(self) -> MyNode:
        current: MyNode = self.first
        while current.next is not None:
            next_el = current.next
            current = next_el
        return current

        