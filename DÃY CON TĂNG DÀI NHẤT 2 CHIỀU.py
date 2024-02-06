from sys import stdin
class So:
    def __init__(self, x, y):
        self.x = x
        self.y = y
input = stdin.readline
ds = []
for _ in range(int(input())):
    x, y = [int(i) for i in input().split()]
    ds.append(So(x,y))
    f = [1]*len(ds)
    ans = -1
    for i in range(len(ds)):
        for j in range(0, i):
            if ds[i].x > ds[j].x and ds[i].y > ds[j].y:
                f[i] = max(f[i], f[j]+1)
        ans = max(ans, f[i])
print(ans)
