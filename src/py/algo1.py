class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def dfs(self, start, visited):
        visited[start] = True
        print(start, end=" ")

        if start in self.graph:
            for neighbor in self.graph[start]:
                if not visited[neighbor]:
                    self.dfs(neighbor, visited)

    def depth_first_search(self, start):
        visited = {node: False for node in self.graph}
        self.dfs(start, visited)


g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

