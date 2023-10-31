# * Mirzohid Abdurazzoqov:
# * 31.10.2023:
from algo1 import g
from algo2 import result, source, destination, result
from algo3 import source, destination, graph, find_all_paths
from algo4 import num_islands, matrix
from algo5 import shortest_distances

print("Task-1:")
g.depth_first_search(2)


print("\n\nTask-2: ")
if result != -1:
    print(f"Shortest path from {source} to {destination} is {result} steps.")
else:
    print("No valid path exists.")

print("\n\nTask-3: ")
print(f"All paths from {source} to {destination}:")
find_all_paths(graph, source, destination)


print("\n\nTask-4: ")
islands_count = num_islands(matrix)
print("Number of islands:", islands_count)


print("\n\nTask-5: ")
print("Shortest distances from source vertex to all vertices:")
for vertex, distance in shortest_distances.items():
    print(f"To vertex {vertex}: Distance = {distance}")
    