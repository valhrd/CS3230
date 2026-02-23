from collections import defaultdict

class Node:
    def __init__(self, val):
        self.val = val
        self.inflows = {}
        self.outflows = {}
        self.is_target = False
        self.visiting = False

    def add_inflow(self, node, capacity):
        self.inflows[node] = [0, capacity]
    
    def add_outflow(self, node, capacity):
        self.outflows[node] = [0, capacity]

def create_graph(vertex_count, edges):
    graph = [Node(i) for i in range(vertex_count)]
    for v1, v2, capacity in edges:
        graph[v1].add_outflow(graph[v2], capacity)
        graph[v2].add_inflow(graph[v1], capacity)
    graph[-1].is_target = True
    return graph

edges_and_capacity = [(0,1,16),(0,2,13),
                      (1,3,12),
                      (2,1,4),(2,4,14),
                      (3,2,9),(3,5,20),
                      (4,3,7),(4,5,4)]
graph = create_graph(6, edges_and_capacity)
starting_node = graph[0]

def ford_fulkerson(starting_node):
    def explore(node, curr_min):
        if node.is_target:
            return True, curr_min
        node.visiting = True
        reached_target = False

        for nb, cap in node.outflows.items():
            if nb.visiting:
                continue
            curr_cap, max_cap = cap
            if max_cap <= curr_cap:
                continue
            reached_target, new_min = explore(nb, min(curr_min, max_cap - curr_cap))
            if reached_target:
                node.outflows[nb][0] += new_min
                nb.inflows[node][0] += new_min
                node.visiting = False
                return True, new_min
        
        for nb, cap in node.inflows.items():
            if nb.visiting:
                continue
            curr_cap, max_cap = cap
            if curr_cap <= 0:
                continue
            reached_target, new_min = explore(nb, min(curr_min, curr_cap))
            if reached_target:
                node.inflows[nb][0] -= new_min
                nb.outflows[node][0] -= new_min
                node.visiting = False
                return True, new_min
        
        node.visiting = False
        return False, curr_min

    prev_max_flow = float('inf')
    max_flow = sum([out[0] for out in starting_node.outflows.values()])
    while prev_max_flow != max_flow:
        prev_max_flow = max_flow
        explore(starting_node, float('inf'))
        max_flow = sum([out[0] for out in starting_node.outflows.values()])

    return max_flow

print(ford_fulkerson(starting_node))