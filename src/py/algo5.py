def dijkstra(graph, source):
    distances = {vertex: float('inf') for vertex in graph}
    distances[source] = 0
    visited = set()

    while len(visited) < len(graph):
        current_vertex = None
        for vertex in graph:
            if vertex not in visited and (current_vertex is None or distances[vertex] < distances[current_vertex]):
                current_vertex = vertex

        visited.add(current_vertex)
        for neighbor, weight in graph[current_vertex].items():
            if distances[current_vertex] + weight < distances[neighbor]:
                distances[neighbor] = distances[current_vertex] + weight

    return distances

# Example usage:
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

source_vertex = 'A'
shortest_distances = dijkstra(graph, source_vertex)