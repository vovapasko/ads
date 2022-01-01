# You have to implement the functions Set(key, value)
#  and Get(key). The function Set(key, value) takes key
#  and value as parameters and assigns the value against
# the provided key. If the key already exists, it updates
#  the value against that key. The function get(key) takes
#  key as a parameter and fetches the value that is stored
#  against that key.


from typing import Dict


class LinkedListNode:
    def __init__(self, key, data):
        self.data = data
        self.key = key
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert_at_head(self, data):
        new_node = LinkedListNode(data)
        if self.head == None:
            self.tail = new_node
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        self.size += 1

    def insert_at_tail(self, key, data):
        new_node = LinkedListNode(key, data)
        if self.tail == None:
            self.tail = new_node
            self.head = new_node
            new_node.next = None
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            new_node.next = None

        self.size += 1

    def remove_node(self, node):
        if node == None:
            return

        if not node.prev == None:
            node.prev.next = node.next

        if not node.next == None:
            node.next.prev = node.prev

        if node == self.head:

            self.head = self.head.next

        if node == self.tail:
            self.tail = self.tail.prev
        self.size = self.size - 1

        return node

    def remove_head(self):
        return self.remove_node(self.head)

    def remove_tail(self):
        return self.remove_node(self.tail)

    def get_head(self):
        return self.head

    def get_tail(self):
        return self.tail


# Linked list operations
# insert_at_tail(self, key, data)
# remove_node(self, node)
# remove_head(self)
# remove_tail(self)
# get_head(self)
# get_tail(self)


class LRU_cache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache: Dict[int, LinkedListNode] = {}
        self.cache_vals = LinkedList()

    def Set(self, key, value):
        # write your code here
        if key not in self.cache:
            if(self.cache_vals.size >= self.capacity):
                self.cache_vals.insert_at_tail(key, value)

                self.cache[key] = self.cache_vals.get_tail()
                del self.cache[self.cache_vals.get_head().key]
                self.cache_vals.remove_head()
            else:
                self.cache_vals.insert_at_tail(key, value)
                self.cache[key] = self.cache_vals.get_tail()

        else:
            self.cache_vals.remove_node(self.cache[key])
            self.cache_vals.insert_at_tail(key, value)
            self.cache[key] = self.cache_vals.get_tail()
        return

    def Get(self, key):
        # write your code here
        if len(self.cache) != 0:
            lru_element = self.cache.get(key, None)
            if lru_element is None:
                return None
            self.cache_vals.remove_head()
            self.cache_vals.insert_at_tail(lru_element.key, lru_element.data)
            return lru_element.data
        return None

    def get_cache(self):
        res = ""
        node = self.cache_vals.head
        while node:
            res += "(" + str(node.key) + "," + str(node.data) + ")"
            node = node.next
        return res
