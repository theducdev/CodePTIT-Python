n = int(input())
a = [[int(i) for i in input().split()] for _ in range(1, n+1)]
k = int(input())
tongtren = 0
for i in range(0, n-1):
    for j in range(i+1, n):
        tongtren+=a[i][j]
tongduoi = 0
for i in range(0, n):
    for j in range(0, i):
        tongduoi+=a[i][j]
if abs(tongtren-tongduoi) <= k:
    print("YES")
else:
    print("NO")
print(abs(tongtren-tongduoi))


