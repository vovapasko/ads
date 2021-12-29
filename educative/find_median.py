# You need to implement a data structure that will store a dynamically
#  growing list of integers and provide efficient access to their median.
# You must implement the functions insert_num(num) and find_median().
# The function insert_num(num) takes the parameter num, which is the
#  number that you need to store. The function find_median() takes no parameter
#  and will return the median of the stored numbers when it’s called.

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

    def fetch(self):
        return self.heap[0]

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

    def __len__(self):
        return len(self.heap)


class MyMaxHeap(MyHeap):
    def __init__(self) -> None:
        super().__init__()

    def insert(self, value: object):
        self.heap.append(value)
        node_index = len(self.heap) - 1
        parent_index = self.get_parent(node_index)
        if parent_index > 0:  # we have more than 1 element
            while self.heap[node_index] > self.heap[parent_index]:
                self.heap[node_index], self.heap[parent_index] = self.heap[parent_index], self.heap[node_index]
                node_index = parent_index
                parent_index = self.get_parent(node_index)


class MyMinHeap(MyHeap):
    def insert(self, value: object):
        self.heap.append(value)
        node_index = len(self.heap) - 1
        parent_index = self.get_parent(node_index)
        if parent_index > 0:  # we have more than 1 element
            while self.heap[node_index] < self.heap[parent_index]:
                self.heap[node_index], self.heap[parent_index] = self.heap[parent_index], self.heap[node_index]
                node_index = parent_index
                parent_index = self.get_parent(node_index)


class MedianOfStream:
    def __init__(self) -> None:
        self.max_heap = MyMaxHeap()
        self.min_heap = MyMinHeap()

    def insert_num(self, num):
        if len(self.min_heap) == 0 and len(self.max_heap) == 0:
            self.max_heap.insert(num)
        elif len(self.min_heap) == 0 and len(self.max_heap) == 1 and num > self.max_heap.fetch():
            prev = self.min_heap.remove()
            self.min_heap.insert(num)
            self.max_heap.insert(prev)
        else:
            if num < self.max_heap.fetch():
                self.min_heap.insert(num)
            else:
                self.max_heap.insert(num)

    def find_median(self):
        # write your code here
        if len(self.max_heap) == len(self.min_heap):
            return (self.max_heap.fetch() + self.min_heap.fetch()) / 2
        else:
            return self.max_heap.fetch()


# Driver code

median_of_A_stream = MedianOfStream()
median_of_A_stream.insert_num(3)
median_of_A_stream.insert_num(1)
print("The median is: " + str(median_of_A_stream.find_median()))
median_of_A_stream.insert_num(5)
print("The median is: " + str(median_of_A_stream.find_median()))
median_of_A_stream.insert_num(4)
print("The median is: " + str(median_of_A_stream.find_median()))
