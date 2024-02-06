n = int(input())
a = [[int(i) for i in input().split()] for _ in range(1, n+1)]
k = int(input())
tongtren = 0
for i in range(0, n):
    for j in range(0, n-i-1):
        tongtren+=a[i][j]

tong = 0
for i in range(0, n):
    for j in range(0, n):
        if i + j != n-1:
            tong+=a[i][j]
tongduoi = tong - tongtren
if abs(tongtren-tongduoi) <= k:
    print("YES")
else:
    print("NO")
print(abs(tongtren-tongduoi))


