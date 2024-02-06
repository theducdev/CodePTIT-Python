dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

m, n = [int(i) for i in input().split()]
f = []
for i in range(0, m):
    a = [int(x) for x in input().split()]
    f.append(a)

ans = set()
for i in range(0, m):
    for j in range(0, n):
        if f[i][j] == -1:
            for k in range(0, 8):
                if i+dx[k] >=0 and i + dx[k] < m and j + dy[k] >=0 and j + dy[k] <n and (f[i+dx[k]][j+dy[k]] > 0 or f[i+dx[k]][j+dy[k]]==-1) :
                    ans.add((i+dx[k], j + dy[k]))
tong = 0
for x in ans:
    tong+=f[x[0]][x[1]]
print(tong)
