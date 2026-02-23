import numpy as np

def greedy_independent_set_size(graph: np.ndarray) -> int:
    # Create a random mapping
    N, _ = graph.shape
    mapping = np.arange(N)
    np.random.shuffle(mapping)

    # Map rows to new enumerations
    enumerated_graph = graph[mapping]
    # Map cols to new enumerations
    enumerated_graph = enumerated_graph[:,mapping]
    
    # Get size of I
    size = 0
    for i in range(N):
        if np.all(enumerated_graph[:i + 1,i] == 0).item():
            size += 1
    return size

def expected_size(graph: np.ndarray) -> float:
    return np.sum(1 / (np.sum(graph, axis=1) + 1)).item()
    
if __name__ == '__main__':
    N = 10
    DISCONNECT_PERCENTAGE = 25

    # Initialise all ones (1 at entry (i, j) represents an edge connecting vertices i and j, 0 otherwise)
    adjacency_matrix = np.ones(N * N, dtype='uint')
    # Randomly disconnect some vertices (to make the graph non-trivial)
    adjacency_matrix[:N * N * DISCONNECT_PERCENTAGE // 100] = 0
    np.random.shuffle(adjacency_matrix)
    # Reshape into an N x N matrix
    adjacency_matrix = adjacency_matrix.reshape((N, N))
    # Get rid of loops from vertices i to themselves
    for i in range(N):
        adjacency_matrix[i, i] = 0

    TRIALS = 10000
    total_size = 0
    for _ in range(TRIALS):
        # Run the same graph over random enumerations of the vertices
        total_size += greedy_independent_set_size(adjacency_matrix)

    experimental_average_size_I = total_size / TRIALS
    print(f"Average size: {experimental_average_size_I}")
    expected_size_I = expected_size(adjacency_matrix)
    print(f"Expected size of I: {expected_size_I}")
    print(f"Error: {abs(experimental_average_size_I - expected_size_I) / expected_size_I * 100:.2f}%")