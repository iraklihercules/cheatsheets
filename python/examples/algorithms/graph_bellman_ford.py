# bellman_ford function: Implements the Bellman-Ford algorithm.
# graph: The weighted graph represented as an adjacency list with the format {vertex: {neighbor: weight}}.
# start: The starting vertex for finding shortest paths.
# The function initializes a dictionary distances to store the shortest distances from the start vertex
# to all other vertices. Initially, all distances are set to infinity, except the distance from the start
# vertex to itself, which is set to 0.
# It iterates through the vertices len(graph) - 1 times, relaxing the edges in each iteration to update
# the distances.
# After the relaxation process, it checks for negative cycles by iterating through all edges once more.
# If a shorter path is found, it indicates the presence of a negative cycle.
# If no negative cycles are detected, it returns the dictionary of shortest distances.
# Example usage: Demonstrates how to use the bellman_ford function to find the shortest distances from
# a specified start vertex to all other vertices in a weighted graph, even in the presence of negative
# edge weights.

# The Bellman-Ford algorithm has a time complexity of O(V * E), where V is the number of vertices and E
# is the number of edges.
# It can handle graphs with negative edge weights and detect negative cycles.

def bellman_ford(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    for _ in range(len(graph) - 1):
        for u in graph:
            for v, weight in graph[u].items():
                if distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight

    # Check for negative cycles
    for u in graph:
        for v, weight in graph[u].items():
            if distances[u] + weight < distances[v]:
                raise ValueError("Graph contains a negative cycle")

    return distances


# Example usage:
if __name__ == "__main__":
    # Example graph represented as an adjacency list with weighted edges
    graph = {
        'A': {'B': 3, 'C': 4},
        'B': {'C': -2},
        'C': {'D': 1},
        'D': {'B': -5}
    }

    start_vertex = 'A'
    shortest_distances = bellman_ford(graph, start_vertex)

    print("Shortest distances from vertex", start_vertex, "to all other vertices:")
    for vertex, distance in shortest_distances.items():
        print(f"To vertex {vertex}: {distance}")
