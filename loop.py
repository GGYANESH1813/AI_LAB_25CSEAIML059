from collections import deque

# Function to perform Breadth First Search
def bfs(graph, start):
    visited = set()          # Stores visited nodes
    queue = deque()          # Create an empty queue

    # Add the starting node
    visited.add(start)
    queue.append(start)

    print("BFS Traversal:")

    # Continue until the queue is empty
    while queue:
        current = queue.popleft()   # Remove front node
        print(current, end=" ")

        # Visit all adjacent nodes
        for neighbour in graph[current]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

# Main Program
if __name__ == "__main__":

    # Graph represented as an adjacency list
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }

    # Starting node
    start_node = 'A'

    # Call BFS function
    bfs(graph, start_node)