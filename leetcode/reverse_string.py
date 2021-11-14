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


def reverseString(s: list):
    stack = MyStack()
    for el in s:
        stack.push(el)
    s = []
    while not stack.is_empty():
        s.append(stack.pop())
    return s


s = ["h", "e", "l", "l", "o"]
a = reverseString(s)
print(a)
