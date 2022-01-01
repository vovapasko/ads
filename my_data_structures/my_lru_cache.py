from typing import Dict


class DoublyNode:
    def __init__(self, key: int, value: int) -> None:
        self.previous = None
        self.key = key
        self.value = value
        self.next = None


class MyLRUCache:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.head = self.tail = None
        self.elements_map: Dict[int, DoublyNode] = dict()

    def get(self, key) -> int:
        lru_element = self.elements_map.get(key, None)
        if lru_element is None:
            return -1
        else:
            tmp = DoublyNode(self.tail.key, self.tail.value)
            self.tail.key = lru_element.key
            self.tail.value = lru_element.value
            lru_element.key = tmp.key
            lru_element.value = tmp.value
            print(self.tail.value)
            return self.tail.value

    def put(self, key, value):
        new_element = DoublyNode(key, value)
        if self.elements_map.get(key, None) is not None:
            return
        if len(self.elements_map) < self.capacity:
            if len(self.elements_map) == 0:
                self.head = self.tail = new_element
            else:
                tmp = self.tail
                tmp.next = new_element
                new_element.previous = tmp
                self.tail = new_element
        else:
            old_head = self.elements_map.pop(self.head.key)
            tmp_head = old_head.next
            self.head = tmp_head
            tmp_tail = self.tail
            tmp_tail.next = new_element
            new_element.previous = tmp_tail
            self.tail = new_element
        self.elements_map[key] = new_element


lRUCache = MyLRUCache(2)
lRUCache.put(1, 1)
lRUCache.put(1, 1)
lRUCache.put(2, 2)
lRUCache.get(1)
lRUCache.put(3, 3)
lRUCache.get(2)
lRUCache.put(4, 4)
lRUCache.get(1)
lRUCache.get(3)
lRUCache.get(4)
