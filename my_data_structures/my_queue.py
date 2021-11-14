class MyQueue:
    def __init__(self) -> None:
        self.container = []

    def enqueue(self, value):
        self.container.append(value)

    def dequeue(self) -> None:
        self.container.pop(0)

    def read(self):
        return self.container[0]


mq = MyQueue()
mq.enqueue(1)
mq.enqueue(2)
mq.enqueue(3)
print(mq.read())
mq.dequeue()
print(mq.read())
