# dijkstra function: Implements Dijkstra's Algorithm.
# graph: The weighted graph represented as an adjacency list with the format {vertex: {neighbor: weight}}.
# start: The starting vertex for finding shortest paths.
# The function initializes a dictionary distances to store the shortest distances from the start
# vertex to all other vertices. Initially, all distances are set to infinity, except the distance
# from the start vertex to itself, which is set to 0.
# It uses a priority queue (implemented with a heap) to store (distance, vertex) pairs, with the
# distance serving as the priority.
# The algorithm iterates through vertices in order of increasing distance from the start vertex.
# For each vertex, it updates the distances to its neighbors if a shorter path is found.
# Finally, it returns the dictionary of shortest distances.
# Example usage: Demonstrates how to use the dijkstra function to find the shortest distances
# from a specified start vertex to all other vertices in a weighted graph.

# Dijkstra's Algorithm is a greedy algorithm that finds the shortest paths from a single source
# vertex to all other
# vertices in a weighted graph with non-negative edge weights. It has a time complexity of O((V + E) log V),
# where V is the number of vertices and E is the number of edges.

import heapq


def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}  # Initialize distances to infinity
    distances[start] = 0  # Distance from start vertex to itself is 0
    heap = [(0, start)]  # Priority queue to store (distance, vertex) pairs

    while heap:
        current_distance, current_vertex = heapq.heappop(heap)

        if current_distance > distances[current_vertex]:
            continue  # Skip if this vertex has already been processed

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))

    return distances


# Example usage:
if __name__ == "__main__":
    # Example graph represented as an adjacency list with weighted edges
    graph = {
        'A': {'B': 3, 'C': 4},
        'B': {'A': 3, 'C': 1, 'D': 7},
        'C': {'A': 4, 'B': 1, 'D': 2},
        'D': {'B': 7, 'C': 2}
    }

    start_vertex = 'A'
    shortest_distances = dijkstra(graph, start_vertex)

    print("Shortest distances from vertex", start_vertex, "to all other vertices:")
    for vertex, distance in shortest_distances.items():
        print(f"To vertex {vertex}: {distance}")
