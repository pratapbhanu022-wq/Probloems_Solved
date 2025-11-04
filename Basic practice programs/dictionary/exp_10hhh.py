# Build an Adjacency List from Edge List (Graph Representation)
edges = [(1, 2), (2, 3), (3, 1), (3, 4)]
graph = {}
for a, b in edges:
    graph.setdefault(a, []).append(b)
    graph.setdefault(b, []).append(a)
print(graph) # {1: [2, 3], 2: [1, 3], 3: [2, 1, 4], 4: [3]}
