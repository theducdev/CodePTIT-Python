import math


def checkSnt(n):
    if n<2: return False
    for i in range(2, int(math.sqrt(n)+1)):
        if n%i==0: return False
    return True

n, m = [int(i) for i in input().split()]
a = [[int(i) for i in input().split()] for _ in range(n)]
maxPrime = 0
for i in range(n):
    for j in range(m):
        if checkSnt(a[i][j]):
            maxPrime = max(maxPrime, a[i][j])

if maxPrime == 0:
    print("NOT FOUND")
else:
    print(maxPrime)
    for i in range(n):
        for j in range(m):
            if a[i][j] == maxPrime:
                print(f"Vi tri [{i}][{j}]")

