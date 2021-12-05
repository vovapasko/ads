class MyVertex:
    def __init__(self, value: str) -> None:
        self.value = value
        self.adjacent_verticies = []

    def __repr__(self) -> str:
        return self.value
