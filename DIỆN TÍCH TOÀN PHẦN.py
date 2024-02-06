dx = [-1,0,0,1]
dy = [0,-1,1,0]
for _ in range(int(input())):
    m, n = [int(i) for i in input().split()]
    h = [0]*(m)
    for i in range(0, m):
        h[i] = [int(i) for i in input().split()]
    sum = 0
    for i in range(m):
        for j in range(n):
           if h[i][j]>0:
               sum+=2
               for k in range(4):
                  if i+dx[k] >= 0 and i + dx[k] < m and j + dy[k] >=0 and j + dy[k] < n:
                       tmp = h[i][j] - h[i+dx[k]][j+dy[k]]
                       if tmp > 0: sum+=tmp
                  else:
                      sum+=h[i][j]
    print(sum)

