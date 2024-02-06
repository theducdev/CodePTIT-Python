def bfs(graph, u, v):
    visited = [False] * (len(graph) + 1)
    queue = deque()
    queue.append(u)
    visited[u] = True

    while queue:
        node = queue.popleft()
        if node == v:
            continue
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

for _ in range(int(intput())):
    n, m, u, v = [int(i) in input().split()]
    ds = []
    ds[i] = []
    for i in range(0, m):
        x, y = [int(i) in input().split()]
        ds[x].append(y)



