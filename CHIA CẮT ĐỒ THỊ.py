from copy import deepcopy
def dfs(ke, u, visited):
    if u not in visited:
        visited.add(u)
        for v in ke[u]:
            dfs(ke, v, visited)

def xoaDinhI(ke, i):
    a = deepcopy(ke)
    a[i].clear()
    for j in range(1, n+1):
        if i in a[j]: a[j].remove(i)
    return a

for _ in range(int(input())):
    ans = {}
    res = 0
    n, m = map(int, input().split())
    ke = {x:[] for x in range(1, n+1)}
    for _ in range(m):
        x, y = map(int, input().split())
        ke[x].append(y)
        ke[y].append(x)
    for i in range(n, 0, -1):
        visited = set()
        cnt= 0
        for j in range(1, n+1):
            if j!=i:
                if j not in visited:
                    cnt+=1
                    dfs(xoaDinhI(ke, i), j, visited)
        ans[cnt]=i
        res = max(res, cnt)
    print(ans[res]) if res > 1 else print(0)
