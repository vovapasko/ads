class MyHeap:
    def __init__(self) -> None:
        self.heap = []

    def remove(self) -> object:
        return self.heap.pop(0)

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
        return self.heap[-1]

    def get_parent(self, node: int):
        return int((node - 1) / 2)

    def get_left_child(self, node: int):
        return (node * 2) + 1

    def get_right_child(self, node: int):
        return (node * 2) + 2


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
heap.insert(40)
