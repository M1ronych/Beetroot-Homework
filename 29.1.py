def dfs_fill_order(v,graph,visited,stack):
    visited.add(v)
    for nei in graph.get(v,[]):
        if nei not in visited:
            dfs_fill_order(nei,graph,visited,stack)
        stack.append(v)

def dfs_collect_scc(v,reversed_graph,visited,component):
    visited.add(v)
    component.append(v)
    for nei in reversed_graph.get(v,[]):
        if nei not in visited:
            dfs_collect_scc(nei,reversed_graph,visited,component)

def reverse_graph(graph):
    reversed_graph = {}
    for v in graph:
        for nei in graph[v]:
            reversed_graph.setdefault(nei,[]).append(v)
    return reversed_graph

def strongly_connected_components(graph):
    visited = set()
    stack = []

    for v in graph:
        if v not in visited:
            dfs_fill_order(v,graph,visited,stack)

    reversed_graph = reverse_graph(graph)

    visited.clear()
    sccs = []

    while stack:
        v = stack.pop()
        if v not in visited:
            component = []
            dfs_collect_scc(v,reversed_graph,visited,component)
            sccs.append(component)

    return sccs


graph = {
    0: [1],
    1: [2],
    2: [0,3],
    3: [4],
    4: [5,3],
    5: []
}

print(strongly_connected_components(graph))




