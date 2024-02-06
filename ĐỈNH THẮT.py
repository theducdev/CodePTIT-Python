def DFS(graph, u, v, visited, path, allPaths):
    visited[u] = True
    path.append(u)

    if u == v:
        # Nếu đã đến đỉnh đích v, thêm đường đi hiện tại vào danh sách các đường đi
        allPaths.append(path.copy())
    else:
        # Nếu chưa đến đỉnh đích, tiếp tục duyệt các đỉnh kề của u
        for neighbor in graph[u]:
            if not visited[neighbor]:
                DFS(graph, neighbor, v, visited, path, allPaths)

    # Quay lui: bỏ đỉnh hiện tại khỏi đường đi để thử các đường khác
    path.pop()
    visited[u] = False

# Hàm chính để tìm tất cả đường đi từ u đến v
def findAllPaths(graph, u, v):
    visited = [False] * (len(graph)+1)
    allPaths = []
    path = []

    DFS(graph, u, v, visited, path, allPaths)

    return allPaths

for _ in range(int(input())):
    n,m,u,v = map(int, input().split())
    ke = {x:[] for x in range(1,n+1)}
    for _ in range(m):
        x,y = map(int, input().split())
        ke[x].append(y)
    allPaths = findAllPaths(ke,u,v)
    z = len(allPaths)
    cnt = 0
    ans = 0
    for i in range(1, n+1):
        cnt=0
        for x in allPaths:
            if i in x:
                cnt+=1
        if cnt == z: ans+=1
    print(ans-2)

