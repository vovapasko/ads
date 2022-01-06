

class LinkedListNode(object):
    def __init__(self, key, value, freq):
        self.key = key
        self.val = value
        self.freq = freq
        self.next = None
        self.prev = None


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, node: LinkedListNode):
        node.next, node.prev = None, None
        if self.head is None:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail
        self.tail = node

    def delete(self, node: LinkedListNode):
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next
        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev
        node.next, node.prev = None, None


class LFU_cache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.cache_vals = LinkedList()

    def Set(self, key, value):
        # if there is no key -> set key: value, set frequency to 1
        # if amount of keys is less than capacity -> add key: value, set frequency to 1
        # if amount equals capacity -> remove less frequent element, set key:value and set
        # frequency to 1

        return

    def Get(self, key):
        # write your code here
        element: LinkedListNode = self.cache.get(key, None)
        if element:
            element.freq += 1
            return element.val
        return -1

    def get_cache(self):
        res = ""
        node = self.cache_vals.head
        while node:
            res += "(" + str(node.key) + "," + str(node.val) + ")"
            node = node.next
        return res
