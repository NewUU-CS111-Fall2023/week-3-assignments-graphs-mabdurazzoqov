def find_all_paths(graph, start, end, path=[]):
    path = path + [start]

    if start == end:
        print("Path:", " -> ".join(map(str, path)))
    for node in graph[start]:
        if node not in path:
            find_all_paths(graph, node, end, path)


graph = {
    0: [1, 2],
    1: [3],
    2: [3],
    3: []
}

source = 2
destination = 3