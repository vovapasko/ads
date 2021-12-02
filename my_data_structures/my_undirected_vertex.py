from my_vertex import MyVertex


class MyUndirectedVertex(MyVertex):
    def __init__(self, value: str) -> None:
        super().__init__(value)

    def connect(self, vertex: MyVertex):
        if self in vertex.adjacent_verticies:
            return
        self.adjacent_verticies.append(vertex)
        vertex.adjacent_verticies.append(self)
