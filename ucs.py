import heapq

def uniform_cost_search(graph, start, goal):
    priority_queue = [(0, start)]
    visited = {}

    while priority_queue:
        cost, node = heapq.heappop(priority_queue)

        if node in visited:
            continue

        visited[node] = cost

        if node == goal:
            return cost

        for neighbour, edge_cost in graph[node]:
            heapq.heappush(priority_queue, (cost + edge_cost, neighbour))

    return float('inf')


graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 5)],
    'C': [('D', 1)],
    'D': []
}

print("Minimum cost to reach D:",
      uniform_cost_search(graph, 'A', 'D'))
