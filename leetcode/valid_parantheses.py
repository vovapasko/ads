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


def isValid(s: str):
    rules = {"(": ")", "{": "}", "[": "]"}
    stack = MyStack()
    for ch in s:
        if ch in rules.keys():
            stack.push(ch)
        else:
            el = stack.pop()
            if el is None:
                return False
            if rules.get(el) != ch:
                return False
    return stack.is_empty()
