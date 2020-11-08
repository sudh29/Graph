# Adjacency List Graph Class
class ListGraph:
    # Constructor
    def __init__(self, nodes):
        self.data = {}
        for node in nodes:
            self.data[node] = []

    # Add the vertex in the Graph
    def add_vertex(self, u, v):
        self.data[u].append(v)

    # Print graph
    def print_graph(self):
        print(self.data)

    # BFS
    def bfs(self, source, nodes):
        path = []
        visited = {}

        q = [source]
        for node in nodes:
            visited[node] = 0

        visited[source] = 1
        path.append(source)

        while len(q) > 0:
            v = q.pop(0)
            for i in range(len(self.data[v])):
                if visited[self.data[v][i]] == 0:
                    q.append(self.data[v][i])
                    visited[self.data[v][i]] = 1
                    path.append(self.data[v][i])
        return path


AdjacencyListGraph = ListGraph(range(8))
AdjacencyListGraph.print_graph()
AdjacencyListGraph.add_vertex(0, 1)
AdjacencyListGraph.add_vertex(0, 2)
AdjacencyListGraph.add_vertex(0, 3)
AdjacencyListGraph.add_vertex(1, 4)
AdjacencyListGraph.add_vertex(1, 5)
AdjacencyListGraph.add_vertex(2, 6)
AdjacencyListGraph.add_vertex(2, 7)
AdjacencyListGraph.add_vertex(3, 7)
AdjacencyListGraph.print_graph()
print()
print(AdjacencyListGraph.bfs(0, range(8)))
