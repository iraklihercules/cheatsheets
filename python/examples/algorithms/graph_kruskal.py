# An example of Kruskal's Algorithm implemented in Python for constructing a minimum
# spanning tree (MST) for a weighted undirected graph:

# DisjointSet class: Implements the disjoint-set data structure (also known as a union-find data structure)
# to keep track of disjoint sets of vertices. It supports two main operations: find (to find the root of a set)
# and union (to merge two sets).
# kruskal function: Implements Kruskal's Algorithm to find the minimum spanning tree (MST) of a given
# weighted undirected graph.
# graph: The weighted graph represented as an adjacency list with the format {vertex: {neighbor: weight}}.
# The function initializes an empty list mst to store the edges of the MST and a set vertices to store
# all vertices in the graph.
# It constructs a list edges containing all edges of the graph, sorted by weight.
# It iterates through the sorted edges and greedily adds edges to the MST if they do not form a cycle.
# The disjoint-set data structure is used to efficiently detect cycles and merge disjoint sets of vertices.

# Example usage: Demonstrates how to use the kruskal function to construct the minimum spanning tree (MST)
# of a given weighted undirected graph.

# Kruskal's Algorithm has a time complexity of O(E * log V), where V is the number of vertices and E is
# the number of edges.
# It efficiently constructs the minimum spanning tree (MST) of a graph by greedily selecting edges with
# the minimum weight
# while ensuring that no cycles are formed.


class DisjointSet:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, vertex):
        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find(self.parent[vertex])
        return self.parent[vertex]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            if self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            elif self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1


def kruskal(graph):
    mst = []  # Minimum spanning tree
    edges = []
    vertices = set()

    for u in graph:
        vertices.add(u)
        for v, weight in graph[u].items():
            edges.append((weight, u, v))

    edges.sort()  # Sort edges by weight

    disjoint_set = DisjointSet(vertices)

    for edge in edges:
        weight, u, v = edge
        if disjoint_set.find(u) != disjoint_set.find(v):
            disjoint_set.union(u, v)
            mst.append((u, v, weight))

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

    minimum_spanning_tree = kruskal(graph)

    print("Minimum Spanning Tree (MST):")
    for edge in minimum_spanning_tree:
        print(f"{edge[0]} - {edge[1]} : {edge[2]}")
