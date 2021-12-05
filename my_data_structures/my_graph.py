from my_vertex import MyVertex


class MyGraph:
    def __init__(self, verticies) -> None:
        self.verticies: list[MyVertex] = verticies

    def make_connection(self, node_with: MyVertex, node_to: MyVertex):
        pass

    def display(self):
        pass

    def bfs(self, start_vertex: MyVertex):
        pass

    def dfs(self, start_vertex: MyVertex):
        pass


class MyUndirectedGraph(MyGraph):
    def __init__(self, verticies) -> None:
        super().__init__(verticies)

    def make_connection(self, node_with: MyVertex, node_to: MyVertex):
        node_with.adjacent_verticies.append(node_to)
        node_to.adjacent_verticies.append(node_with)

    def display(self):
        for vertex in self.verticies:
            print(vertex.value + " -> ", end=" ")
            for adj in vertex.adjacent_verticies:
                print(adj.value + " -> ", end=" ")
            print()

    def dfs(self, start_vertex: MyVertex, visited={}):
        print(start_vertex.value)
        visited[start_vertex.value] = True
        for node in start_vertex.adjacent_verticies:
            if not visited.get(node.value, False):
                self.dfs(node, visited)


n0 = MyVertex("0")
n1 = MyVertex("1")
n2 = MyVertex("2")
n3 = MyVertex("3")
n4 = MyVertex("4")
n5 = MyVertex("5")
n6 = MyVertex("6")
n7 = MyVertex("7")
n8 = MyVertex("8")


graph = MyUndirectedGraph([n0, n1, n2, n3, n4, n5, n6, n7, n8])
graph.make_connection(n0, n1)
graph.make_connection(n0, n2)
graph.make_connection(n0, n3)
graph.make_connection(n0, n4)
graph.make_connection(n1, n5)
graph.make_connection(n5, n6)
graph.make_connection(n2, n6)
graph.make_connection(n3, n7)
graph.make_connection(n7, n8)
graph.dfs(n0)
