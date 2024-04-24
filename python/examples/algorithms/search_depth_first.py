# dfs function: Implements the Depth-First Search (DFS) algorithm.
# graph: The graph represented as an adjacency list.
# start: The starting node for the DFS traversal.
# visited: A set to keep track of visited nodes to avoid revisiting them.
# The function starts by adding the starting node to the visited set and prints it.
# Then, it recursively explores each neighbor of the starting node that has not been visited yet, applying DFS.

# DFS explores as far as possible along each branch before backtracking.
# It can be implemented using either recursion or iteration (using a stack).
# This example uses recursion to traverse the graph starting from a specified node.

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=" ")

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


# Example usage:
if __name__ == "__main__":
    # Example graph represented as an adjacency list
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

    print("Depth-First Search (DFS):")
    dfs(graph, 'A')  # Output: A B D E F C
