def is_valid(x, y, grid):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 1


def shortest_path(grid, source, destination):
    if not grid:
        return -1  # Invalid grid

    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]

    def bfs(x, y):
        queue = [(x, y, 0)]

        while queue:
            x, y, distance = queue.pop(0)
            visited[x][y] = True

            if (x, y) == destination:
                return distance

            neighbors = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
            for nx, ny in neighbors:
                if is_valid(nx, ny, grid) and not visited[nx][ny]:
                    queue.append((nx, ny, distance + 1))

        return -1  # No path found

    return bfs(source[0], source[1])



grid = [
    [1, 1, 0, 1, 1],
    [1, 1, 1, 1, 0],
    [1, 0, 0, 1, 1],
    [1, 1, 1, 0, 1]
]

source = (0, 0)
destination = (3, 4)

result = shortest_path(grid, source, destination)
