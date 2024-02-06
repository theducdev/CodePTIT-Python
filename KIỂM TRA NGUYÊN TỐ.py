f = [1]*1005
f[0] = 0
f[1] = 0
f[2] = 1
for i in range(2, 1000):
    if f[i] == 1:
        for j in range(i*i, 1000, i):
            f[j] = 0

n, m = [int(i) for i in input().split()]
a = [[0]]*n
for i in range(n):
    a[i] = [f[int(i)] for i in input().split()]

for i in range(n):
    print(*a[i], sep=" ")
