# bfs function: Implements the Breadth-First Search (BFS) algorithm.
# graph: The graph represented as an adjacency list.
# start: The starting node for the BFS traversal.
# visited: A set to keep track of visited nodes to avoid revisiting them.
# queue: A deque (double-ended queue) to store the nodes to be visited next in the BFS traversal.
# The function starts by adding the starting node to the queue and marking it as visited.
# Then, it enters a loop where it dequeues a node from the front of the queue, prints it, and adds
# its unvisited neighbors to the queue.

# BFS explores all neighbor nodes at the current depth before moving to the next depth level.
# It is commonly implemented using a queue data structure to keep track of the nodes to be visited next.
# This example uses a deque from the collections module as the queue.

from collections import deque


def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            queue.extend(graph[node])


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

    print("Breadth-First Search (BFS):")
    bfs(graph, 'A')  # Output: A B C D E F
