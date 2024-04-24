# _init__: Initializes the graph with an empty adjacency list.
# add_edge(u, v): Adds an edge between nodes u and v to the graph's adjacency list.
# dfs(start_node): Performs a Depth First Search (DFS) traversal starting from the start_node.
# bfs(start_node): Performs a Breadth First Search (BFS) traversal starting from the start_node.

# In this example, the graph is represented using an adjacency list, where each node is a key
# in the dictionary graph, and its corresponding value is a list of its adjacent nodes.
# The dfs and bfs methods traverse the graph starting from a given node using Depth First Search and
# Breadth First Search, respectively.

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def dfs(self, start_node):
        visited = set()

        def dfs_helper(node):
            visited.add(node)
            print(node, end=" ")

            if node in self.graph:
                for neighbor in self.graph[node]:
                    if neighbor not in visited:
                        dfs_helper(neighbor)

        dfs_helper(start_node)

    def bfs(self, start_node):
        visited = set()
        queue = []

        queue.append(start_node)
        visited.add(start_node)

        while queue:
            current_node = queue.pop(0)
            print(current_node, end=" ")

            if current_node in self.graph:
                for neighbor in self.graph[current_node]:
                    if neighbor not in visited:
                        queue.append(neighbor)
                        visited.add(neighbor)


# Example usage:
if __name__ == "__main__":
    graph = Graph()
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 2)
    graph.add_edge(2, 0)
    graph.add_edge(2, 3)
    graph.add_edge(3, 3)

    print("Depth First Traversal (DFS):")
    graph.dfs(2)  # Output: 2 0 1 3

    print("\nBreadth First Traversal (BFS):")
    graph.bfs(2)  # Output: 2 0 3 1
