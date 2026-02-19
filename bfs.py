from collections import deque

graph = {
    1: [2, 3],
    2: [4],
    3: [4],
    4: [5],
    5: []
}

start = 1
goal = 5

queue = deque([start])
visited = [start]
parent = {}

while queue:
    node = queue.popleft()

    if node == goal:
        break

    for neighbour in graph[node]:
        if neighbour not in visited:
            visited.append(neighbour)
            parent[neighbour] = node
            queue.append(neighbour)

path = []
node = goal

while node != start:
    path.append(node)
    node = parent[node]

path.append(start)
path.reverse()

print("Shortest path:", path)
