
# Create Stack => stack = myStack(5); where 5 is size of stack
# Create Queue => queue = myQueue(5); where 5 is size of queue
# Stack Functions => isEmpty(), isFull(), top()
# Queue Functions => enqueue(int),dequeue(),isEmpty(),getSize()

class my_stack:
    def __init__(self):
        self.stack_list = []

    def is_empty(self):
        return len(self.stack_list) == 0

    def top(self):
        if self.is_empty():
            return None
        return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        if self.is_empty():
            return None
        return self.stack_list.pop()


class min_stack:
    # Constructor
    def __init__(self):
        self.stack_list = []
        self.min_stack_list = my_stack()

    def size(self):
        return len(self.stack_list)

    def is_empty(self):
        return len(self.stack_list) == 0

    def push(self, value):
        if self.is_empty():
            self.min_stack_list.push(value)
        elif value < self.min_stack_list.top():
            self.min_stack_list.push(value)
        self.stack_list.append(value)

    def pop(self):
        element = self.stack_list.pop()
        if element == self.min_stack_list.top():
            self.min_stack_list.pop()
        if self.is_empty():
            return None
        return

    def min(self):
        # Write your code here
        return self.min_stack_list.top()
