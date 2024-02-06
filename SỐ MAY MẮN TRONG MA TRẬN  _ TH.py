import math



n, m = [int(i) for i in input().split()]
a = [[int(i) for i in input().split()] for _ in range(n)]
maxMT = 0
minMT = 999999999
for i in range(n):
    for j in range(m):
        maxMT = max(maxMT, a[i][j])
        minMT = min(minMT, a[i][j])
target = maxMT-minMT
check = 0
for i in range(n):
    for j in range(m):
        if a[i][j] == target:
            check = 1
            break
if check == 0:
    print("NOT FOUND")
else:
    print(target)
    for i in range(n):
        for j in range(m):
            if a[i][j] == target:
                print(f"Vi tri [{i}][{j}]  ")

