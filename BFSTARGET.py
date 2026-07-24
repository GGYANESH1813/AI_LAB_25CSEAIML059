from collections import deque

# Function to perform BFS Search
def bfs_search(graph, start, target):

    # Step 1: Create an empty list called visited
    visited = []

    # Step 2: Create an empty queue
    queue = deque()

    # Step 3: Put the start node into the queue
    queue.append(start)

    # Step 4: Mark the start node as visited
    visited.append(start)

    # Step 4.1: While the queue is not empty
    while queue:

        # Step 4.1.1: Pop the first node from the queue
        current_node = queue.popleft()

        # Step 4.1.2: Print the current node
        print(current_node, end=" ")

        # Step 4.1.3: Check if current node is the target
        if current_node == target:
            print("\nTarget found!")
            return

        # Step 4.2: Visit all neighbours
        for neighbour in graph[current_node]:

            # Step 4.2.1: If neighbour is not visited
            if neighbour not in visited:

                # Step 4.2.2: Mark as visited
                visited.append(neighbour)

                # Step 4.2.3: Add to queue
                queue.append(neighbour)

    # Step 5: Target not found
    print("\nTarget not found!")


# Example Graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Start and Target Nodes
start_node = 'A'
target_node = 'E'

print("BFS Search Traversal:")
bfs_search(graph, start_node, target_node)