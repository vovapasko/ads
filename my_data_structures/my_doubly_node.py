class MyDoublyNode:
    def __init__(self, value, previous_el = None, next_el = None) -> None:
        self.value = value
        self.previous = previous_el
        self.next = next_el