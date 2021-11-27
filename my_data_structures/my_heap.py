class MyHeap:
    def __init__(self) -> None:
        self.heap = []

    def remove(self) -> object:
        if len(self.heap) == 1:
            return self.heap.pop()
        else:
            to_remove = self.heap[0]
            self.heap[0] = self.last()
            node_index = 0
            child_index = self.get_greater_child_index(node_index)
            while child_index is not None:
                self.heap[node_index], self.heap[child_index] = self.heap[child_index], self.heap[node_index]
                node_index = child_index
                child_index = self.get_greater_child_index(node_index)
            return to_remove

    def insert(self, value: object):
        self.heap.append(value)
        node_index = len(self.heap) - 1
        parent_index = self.get_parent(node_index)
        if parent_index > 0:  # we have more than 1 element
            while self.heap[node_index] > self.heap[parent_index]:
                self.heap[node_index], self.heap[parent_index] = self.heap[parent_index], self.heap[node_index]
                node_index = parent_index
                parent_index = self.get_parent(node_index)

    def last(self):
        return self.heap.pop()

    def get_parent(self, node: int):
        return int((node - 1) / 2)

    def get_left_child(self, node: int):
        return (node * 2) + 1

    def get_right_child(self, node: int):
        return (node * 2) + 2

    def get_greater_child_index(self, node_index: int):
        left_index = self.get_left_child(node_index)
        right_index = self.get_right_child(node_index)
        if left_index < len(self.heap) and right_index < len(self.heap):
            if self.heap[left_index] < self.heap[right_index]:
                return right_index
            if self.heap[left_index] > self.heap[right_index]:
                return left_index
            else:
                return None


def init_heap():
    heap = MyHeap()
    heap.insert(100)
    heap.insert(88)
    heap.insert(25)
    heap.insert(87)
    heap.insert(16)
    heap.insert(8)
    heap.insert(12)
    heap.insert(86)
    heap.insert(50)
    heap.insert(2)
    heap.insert(15)
    heap.insert(3)
    return heap


heap = init_heap()
# heap.insert(40)
heap.remove()
heap.remove()
