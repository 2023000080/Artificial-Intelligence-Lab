from collections import deque

def water_jug_bfs(jug1, jug2, target):
    visited = set()
    queue = deque([(0, 0)])

    while queue:
        x, y = queue.popleft()

        if (x, y) in visited:
            continue

        visited.add((x, y))
        print("Visited:", (x, y))

        if x == target or y == target:
            print("Goal reached:", (x, y))
            return

        # Fill jug1
        queue.append((jug1, y))

        # Fill jug2
        queue.append((x, jug2))

        # Empty jug1
        queue.append((0, y))

        # Empty jug2
        queue.append((x, 0))

        # Transfer jug1 → jug2
        transfer = min(x, jug2 - y)
        queue.append((x - transfer, y + transfer))

        # Transfer jug2 → jug1
        transfer = min(y, jug1 - x)
        queue.append((x + transfer, y - transfer))


# Example call
water_jug_bfs(4, 3, 2)