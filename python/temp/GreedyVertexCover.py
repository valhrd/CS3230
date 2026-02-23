from typing import *
from heapq import *
import random
from typing import Dict
import time
import matplotlib.pyplot as plt

def convert_to_graph(v_count: int, edges: List[List[int]]):
    graph = {v: set() for v in range(v_count)}
    for a, b in edges:
        graph[a].add(b)
        graph[b].add(a)
    return graph

def create_random_graph(vertex_count, threshold):
    edges = []
    for i in range(vertex_count):
        for j in range(i + 1, vertex_count):
            r = random.uniform(0, 1)
            if r <= threshold:
                edges.append([i, j])
    return convert_to_graph(vertex_count, edges), edges

class VertexCover():
    def __init__(self, graph: Dict, edges: List[List[int]]):
        self.graph = graph
        self.edges = self.setify_edges(edges)
        self.vertex_count = len(graph)

    def setify_edges(self, edges):
        return {tuple(sorted(edge)) for edge in edges}
    
    def process_graph(self):
        copy = {}
        for v, nbs in self.graph.items():
            if len(nbs) != 0:
                copy[v] = nbs.copy()
        return copy
    
    def produce_vertex_cover(self):
        pass

class IncidentGreedyVertexCover(VertexCover):
    def produce_vertex_cover(self):
        vertex_cover = []
        processed_graph = self.process_graph()

        max_heap = [(-len(nbs), v) for v, nbs in processed_graph.items()]
        heapify(max_heap)

        while max_heap:
        
            _, most_incident_vertex = heappop(max_heap)
            vertex_cover.append(most_incident_vertex)

            first_order_nb = set()
            second_order_nb = set()

            for nb in processed_graph[most_incident_vertex]:
                first_order_nb.add(nb)
                for nbnb in processed_graph[nb]:
                    second_order_nb.add(nbnb)
                processed_graph.pop(nb)

            processed_graph.pop(most_incident_vertex)

            first_order_nb.add(most_incident_vertex)

            for v in first_order_nb:
                if v in second_order_nb:
                    second_order_nb.remove(v)
            
            for nbnb in second_order_nb:
                for nb in first_order_nb:
                    if nb in processed_graph[nbnb]:
                        processed_graph[nbnb].remove(nb)

            max_heap = [(-len(nbs), v) for v, nbs in processed_graph.items()]
            heapify(max_heap)

        return vertex_cover
    
class EdgeGreedyVertexCover(VertexCover):    
    def produce_vertex_cover(self):
        processed_graph = self.process_graph()
        edge_set = self.edges.copy()
        vertex_cover = set()

        max_heap = [
            (-len(processed_graph[v1]) - len(processed_graph[v2]), v1, v2)
            for v1, v2 in edge_set
        ]
        heapify(max_heap)

        while max_heap:
            _, v1, v2 = heappop(max_heap)
            vertex_cover.add(v1)
            vertex_cover.add(v2)

            neighbors = set(processed_graph[v1]).union(set(processed_graph[v2]))
            for neighbor in neighbors:
                if neighbor in processed_graph:
                    processed_graph[neighbor] -= {v1, v2}
            
            processed_graph.pop(v1, None)
            processed_graph.pop(v2, None)

            edge_set -= {tuple(sorted((v1, nb))) for nb in neighbors}
            edge_set -= {tuple(sorted((v2, nb))) for nb in neighbors}

            max_heap = [
                (-len(processed_graph[v1]) - len(processed_graph[v2]), v1, v2)
                for v1, v2 in edge_set
            ]
            heapify(max_heap)
        
        return list(vertex_cover)

class StandardGreedyVertexCover(VertexCover):
    def produce_vertex_cover(self):
        edges = list(self.edges.copy())
        random.shuffle(edges)
        edge_set = set(edges)
        vertex_cover = set()
        
        while edge_set:
            v1, v2 = list(edge_set)[0]
            vertex_cover.add(v1)
            vertex_cover.add(v2)

            neighbours = self.graph[v1].union(self.graph[v2])
            adjacent_edges = set()

            for nb in neighbours:
                for v in [v1, v2]:
                    temp = tuple(sorted([nb, v]))
                    adjacent_edges.add(temp)
            
            edge_set = edge_set.difference(adjacent_edges)
        
        return list(vertex_cover)
    
class NPVertexCover(VertexCover):    
    def produce_vertex_cover(self):
        vertex_cover = []
        for depth_limit in range(self.vertex_count):
            if self.depth_limited_search(vertex_cover, 0, depth_limit, 0):
                break
        return vertex_cover
    
    def depth_limited_search(self, vertex_cover, depth, limit, start):
        if self.is_cover(vertex_cover):
            return True
        if depth > limit:
            return False
        for i in range(start, self.vertex_count):
            if len(self.graph[i]) == 0:
                continue
            vertex_cover.append(i)
            if self.depth_limited_search(vertex_cover, depth + 1, limit, i + 1):
                return True
            vertex_cover.pop()
        return False
    
    def is_cover(self, vertex_cover):
        for v1, v2 in self.edges:
            if v1 not in vertex_cover and v2 not in vertex_cover:
                return False
        return True
    
def print_graph(graph):
    for k in range(len(graph)):
        print(k, graph[k])

vertex_count = 20
threshold = 0.75
# edges = [[1,2], [2,3], [3,4], [3,5]]
# graph = convert_to_graph(vertex_count, edges)

# print(graph)
# igvc = IncidentGreedyVertexCover(graph)
# egvc = EdgeGreedyVertexCover(graph, edges)
# npvc = NPVertexCover(graph)

# print(igvc.produce_vertex_cover())
# print(egvc.produce_vertex_cover())
# print(npvc.produce_vertex_cover())
total_greedy_ratio = 0
total_standard_ratio = 0
iterations = 100

eg_two_approx = True
sr_two_approx = True

eg_smaller_count = 0
sr_smaller_count = 0

eg_total_time = 0
sr_total_time = 0

x = []
eg_times = []
sr_times = []

for vertex_count in range(20, 105, 5):
    for _ in range(iterations):
        graph, edges = create_random_graph(vertex_count, threshold)

        gvc = EdgeGreedyVertexCover(graph, edges)
        svc = StandardGreedyVertexCover(graph, edges)
        # npvc = NPVertexCover(graph, edges)

        start = time.time()
        greedy_vertex_cover = gvc.produce_vertex_cover()
        eg_total_time += time.time() - start

        start = time.time()
        standard_vertex_cover = svc.produce_vertex_cover()
        sr_total_time += time.time() - start
        
        # np_vertex_cover = npvc.produce_vertex_cover()

        # g = len(greedy_vertex_cover)
        # s = len(standard_vertex_cover)
        # n = len(np_vertex_cover)
        
        # eg_two_approx &= (n <= g <= 2 * n)
        # sr_two_approx &= (n <= s <= 2 * n)

        # total_greedy_ratio += g / n
        # total_standard_ratio += s / n

        # if g < s:
        #     eg_smaller_count += 1
        # if g > s:
        #     sr_smaller_count += 1
        
    # print("Average EdgeGreedy to Optimal Ratio: ", total_greedy_ratio / iterations, "| All 2-Approximation: ", eg_two_approx, "| Count: ", eg_smaller_count)
    # print("Average RandomStandard to Optimal Ratio: ", total_standard_ratio / iterations, "| All 2-Approximation: ", sr_two_approx, "| Count: ", sr_smaller_count)
    print("Vertices: ", vertex_count)
    print("Average EdgeGreedy Time ", eg_total_time / iterations)
    print("Average RandomStandard Time: ", sr_total_time / iterations)
    
    x.append(vertex_count)
    eg_times.append(eg_total_time / iterations)
    sr_times.append(sr_total_time / iterations)

plt.plot(x, eg_times, label = "EdgeGreedyVC")
plt.plot(x, sr_times, label = "StandardRandomVC")
plt.title("Avg Times")
plt.legend()
plt.show()