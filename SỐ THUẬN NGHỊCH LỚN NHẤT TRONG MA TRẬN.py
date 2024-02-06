import math


def checkThuanNghich(n):
    if n < 10: return False
    x = str(n)
    for i in range(int(len(x)/2)+1):
        if x[i]!= x[len(x)-1-i]:
            return False
    return True


n, m = [int(i) for i in input().split()]
a = [[int(i) for i in input().split()] for _ in range(n)]
maxTN = 0
for i in range(n):
    for j in range(m):
        if checkThuanNghich(a[i][j]):
            maxTN = max(maxTN, a[i][j])

if maxTN == 0:
    print("NOT FOUND")
else:
    print(maxTN)
    for i in range(n):
        for j in range(m):
            if a[i][j] == maxTN:
                print(f"Vi tri [{i}][{j}]")

