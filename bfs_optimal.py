from collections import deque

graph = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'C': [],
    'D': ['G', 'H'],
    'E': ['I', 'J'],
    'F': [],
    'G': ['K', 'L'],
    'H': [],
    'I': [],
    'J': [],
    'K': [],
    'L': []
}

def bfs(start):
    visited = set()
    queue = deque([start])
    print("Dequeued\tEnqueued")
    visited.add(start)

    while queue:
        node = queue.popleft()
        enqueued = []

        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
                enqueued.append(neighbour)

        print(f"{node}\t\t{', '.join(enqueued) if enqueued else '-'}")

bfs('A')
