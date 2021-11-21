class MyStack:
    def __init__(self) -> None:
        self.container = []

    def push(self, value) -> None:
        self.container.append(value)

    def pop(self) -> object:
        try:
            return self.container.pop(-1)
        except IndexError:
            return None

    def read(self) -> object:
        try:
            return self.container[-1]
        except IndexError:
            return None

    def is_empty(self):
        return len(self.container) == 0


# ms = MyStack()
# # ms.push(1)
# # ms.push(2)
# # ms.push(3)
# print(ms.read())
# ms.pop()
# print(ms.read())
