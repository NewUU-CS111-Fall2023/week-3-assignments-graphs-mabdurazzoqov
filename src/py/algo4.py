def num_islands(grid):
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    num_islands = 0

    def dfs(x, y):
        if 0 <= x < rows and 0 <= y < cols and grid[x][y] == "1":
            grid[x][y] = "0"
            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "1":
                num_islands += 1
                dfs(i, j)

    return num_islands


matrix = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]