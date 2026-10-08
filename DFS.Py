# Depth First Search (DFS) using User Input

def dfs(graph, start_node):
    visited = []               # List to store visited nodes
    stack = [start_node]       # Stack initialized with the starting node

    while stack:
        current_node = stack.pop()   # Remove the last node from the stack

        if current_node not in visited:
            print(f"Exploring Node: {current_node}")
            visited.append(current_node)

            # Add all unvisited neighbors to the stack
            # Reverse is used to maintain natural traversal order
            for neighbor in reversed(graph.get(current_node, [])):
                if neighbor not in visited:
                    stack.append(neighbor)

    return visited


# ---------------- User Input Section ----------------

print("========== DFS Graph Creation ==========")

student_graph = {}

# Input the number of edges
num_edges = int(input("Enter the number of edges (connections): "))

# Input each edge
for i in range(num_edges):
    print(f"\nEdge {i + 1}")

    u = input("Enter Starting Node: ")
    v = input("Enter Ending Node: ")

    # Create empty lists if nodes are not already present
    if u not in student_graph:
        student_graph[u] = []

    if v not in student_graph:
        student_graph[v] = []

    # Since the graph is undirected
    student_graph[u].append(v)
    student_graph[v].append(u)

# Display the graph
print("\nGraph Dictionary:")
print(student_graph)

# Input starting node for DFS
start = input("\nEnter the Starting Node for DFS: ")

print("\n========== DFS Traversal ==========")

# Perform DFS
visited_nodes = dfs(student_graph, start)

# Display visited nodes
print("\nDFS Traversal Order:", visited_nodes)