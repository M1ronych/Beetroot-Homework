from collections import deque

def bfs_shortest_paths(graph,start):
    dist = {v: float('inf') for v in graph}
    dist[start] = 0
    queue = deque([start])

    while queue:
        v = queue.popleft()
        for nei in graph[v]:
            if dist[nei] == float('inf'):
                dist[nei] = dist[v] + 1
                queue.append(nei)

    return dist

def all_pairs_shortest_paths(graph):
    return {v: bfs_shortest_paths(graph,v) for v in graph}

if __name__ == "__main__":
    graph = {
        0: [1,2],
        1: [0,2,3],
        2: [0,1,3],
        3: [1,2]
    }

distances = all_pairs_shortest_paths(graph)

for v in distances:
    print(f"From {v}: {distances[v]}")


