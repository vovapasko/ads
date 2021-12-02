class MyVertex:
    def __init__(self, value: str) -> None:
        self.value = value
        self.adjacent_verticies = []

    def insert(self, vertex):
        self.adjacent_verticies.append(vertex)
