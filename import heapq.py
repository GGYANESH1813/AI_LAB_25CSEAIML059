import heapq

def a_star(graph, heuristic, start, goal):
    open_list = []
    heapq.heappush(open_list, (heuristic[start], 0, start, [start]))

    g_cost = {start: 0}

    while open_list:
        f, g, current, path = heapq.heappop(open_list)

        if current == goal:
            return path, g

        for neighbor, cost in graph[current]:
            new_g = g + cost

            if neighbor not in g_cost or new_g < g_cost[neighbor]:
                g_cost[neighbor] = new_g
                new_f = new_g + heuristic[neighbor]

                heapq.heappush(
                    open_list,
                    (new_f, new_g, neighbor, path + [neighbor])
                )

    return None, float("inf")


graph = {
    'S': [('A', 1), ('G', 10)],
    'A': [('B', 2), ('C', 1)],
    'B': [('D', 5)],
    'C': [('D', 3), ('G', 4)],
    'D': [('G', 2)],
    'G': []
}

heuristic = {
    'S': 5,
    'A': 3,
    'B': 4,
    'C': 2,
    'D': 6,
    'G': 0
}

path, cost = a_star(graph, heuristic, 'S', 'G')

print("Optimal Path:", " -> ".join(path))
print("Total Cost:", cost)