# Function to take heuristic values
def input_heuristics():
    heuristic = {}

    n = int(input("Enter the number of nodes: "))

    for i in range(n):
        node = input(f"Enter node {i+1} name: ").strip().upper()
        h = int(input(f"Enter heuristic value for {node}: "))
        heuristic[node] = h

    return heuristic


# Function to take graph edges
def input_graph():
    graph = {}

    e = int(input("\nEnter the number of edges: "))

    for i in range(e):
        u = input("Enter source node: ").strip().upper()
        v = input("Enter destination node: ").strip().upper()
        cost = int(input("Enter edge cost: "))

        if u not in graph:
            graph[u] = []

        graph[u].append((v, cost))

    return graph


# Function to display heuristic values
def display_heuristics(heuristic):
    print("\nHeuristic Values:")
    for node, value in heuristic.items():
        print(f"{node} : {value}")


# Function to display graph
def display_graph(graph):
    print("\nGraph:")

    for node in graph:
        print(f"{node} --> {graph[node]}")


# Main Function
def main():
    heuristic = input_heuristics()
    graph = input_graph()

    display_heuristics(heuristic)
    display_graph(graph)


# Program starts here
main()