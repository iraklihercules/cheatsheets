# An example of Prim's Algorithm implemented in Python for constructing a minimum spanning
# tree (MST) for a weighted undirected graph:

# prim function: Implements Prim's Algorithm to find the minimum spanning tree (MST) of a given
# weighted undirected graph.
# graph: The weighted graph represented as an adjacency list with the format {vertex: {neighbor: weight}}.
# start: The starting vertex for constructing the MST.
# The function initializes an empty list mst to store the edges of the MST and a set visited to keep
# track of visited vertices.
# It starts from the start vertex and iteratively adds the minimum-weight edge connecting a visited
# vertex to an unvisited vertex to the MST.
# The function uses a heap (edges) to efficiently select the minimum-weight edge to add to the MST.
# The process continues until all vertices are visited.

# Example usage: Demonstrates how to use the prim function to construct the minimum spanning tree (MST)
# of a given weighted undirected graph.

# Prim's Algorithm has a time complexity of O(E * log V), where V is the number of vertices and E is
# the number of edges.
# It efficiently constructs the minimum spanning tree (MST) of a graph by greedily selecting edges with
# the minimum weight.


import heapq


def prim(graph, start):
    mst = []  # Minimum spanning tree
    visited = set([start])  # Set to keep track of visited vertices
    edges = [(weight, start, neighbor) for neighbor, weight in graph[start].items()]
    heapq.heapify(edges)  # Convert the list of edges into a heap

    while edges:
        weight, u, v = heapq.heappop(edges)
        if v not in visited:
            visited.add(v)
            mst.append((u, v, weight))

            for neighbor, weight in graph[v].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (weight, v, neighbor))

    return mst


# Example usage:
if __name__ == "__main__":
    # Example graph represented as an adjacency list with weighted edges
    graph = {
        'A': {'B': 2, 'C': 3},
        'B': {'A': 2, 'C': 1, 'D': 1},
        'C': {'A': 3, 'B': 1, 'D': 2},
        'D': {'B': 1, 'C': 2}
    }

    start_vertex = 'A'
    minimum_spanning_tree = prim(graph, start_vertex)

    print("Minimum Spanning Tree (MST):")
    for edge in minimum_spanning_tree:
        print(f"{edge[0]} - {edge[1]} : {edge[2]}")
