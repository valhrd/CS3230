from heapq import *
import random

# Algorithm assumes graph given is not disconnected and is simple
def prims(node_num: int, edges: list[list[int]]) -> list[list[int]]:
    # Convert to a graph to dict form
    graph = create_dict_graph(edges)
    assert validate_graph(graph)
    assert node_num == len(graph)

    seen_vertices = {0}
    edges_minheap = [(graph[0][v], 0, v) for v in graph[0]]
    mst_edges = []
    heapify(edges_minheap)

    while edges_minheap:
        weight, u, v = heappop(edges_minheap)
        if u in seen_vertices and v in seen_vertices:
            continue

        if u not in seen_vertices:
            seen_vertices.add(u)
            for x in graph[u]:
                if x not in seen_vertices:
                    heappush(edges_minheap, (graph[u][x], u, x))

        if v not in seen_vertices:
            seen_vertices.add(v)
            for x in graph[v]:
                if x not in seen_vertices:
                    heappush(edges_minheap, (graph[v][x], v, x))

        mst_edges.append((u, v, weight))
    
    print(mst_edges)
    return sum(w for _, _, w in mst_edges)

def create_dict_graph(edges: list[list[int]]) -> dict:
    graph = {}
    for u, v, w in edges:
        if u not in graph:
            graph[u] = {}
        if v not in graph:
            graph[v] = {}
        graph[u][v] = w
        graph[v][u] = w
    return graph

# DFS through graph to check if it is simple and connected
def validate_graph(graph: dict) -> bool:
    n = len(graph)
    start = list(graph.keys())[0]
    stack = [start]
    seen = {start}
    while stack:
        curr = stack.pop()
        for nb in graph[curr]:
            # Reject if there are loops (graph is not simple)
            if curr == nb:
                return False
            if nb in seen:
                continue
            seen.add(nb)
            stack.append(nb)
    return n == len(seen)

if __name__ == '__main__':
    edges = [
        [0, 1, 6],
        [0, 2, 5],
        [0, 3, 8],
        [0, 4, 14],
        [1, 2, 12],
        [2, 5, 9],
        [2, 6, 7],
        [3, 4, 3],
        [3, 6, 10],
        [6, 7, 15],
    ]
    print(prims(8, edges))