
def dfs(ke, u, visited):
    if u not in visited:
        visited.add(u)
        for v in ke[u]:
            dfs(ke, v, visited)

for _ in range(1):
    n = int(input())
    m = int(input())
    ke = {x:[] for x in range(1, n+1)}
    for _ in range(m):
        x, y = map(int, input().split())
        ke[x].append(y)
        ke[y].append(x)
    visited = set()
    dfs(ke, u, visited)
    for i in range(1,n+1):
        if i not in visited:
            print(i)



