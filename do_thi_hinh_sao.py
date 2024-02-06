N = int(input())
tmp = 0
check = 0
ke = [[] for _ in range(N+1)]
for _ in range (N-1):
    x, y = [int(i) for i in input().split()]
    ke[x].append(y)
    ke[y].append(x)
for x in ke:
    if len(x) == N-1:
        check = 1
if check:
    print("Yes")
else:
    print("No")
