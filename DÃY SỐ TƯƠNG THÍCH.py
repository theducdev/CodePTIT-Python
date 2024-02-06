import math

def timXtrongdoan(a, b):
    ds = []
    for x in range(math.floor(a), math.ceil(b)-1, -1):
        ds.append(x)
    return min(ds) if ds else 0


n = int(input())
ds = [int(i) for i in input().split()]
x = min(ds)
sum = 0
ans = 10**9
chia = set()
for i in range(1, x+1):
    chia.add(math.floor(x/i))

for i in chia:
    # print(f"{i}: ", end=" ")
    sum = 0
    for j in ds:
        tmp = timXtrongdoan(j/i, j/(i+1-0.01))
        # print(tmp, end=" ")
        if tmp == 0:
            tmp+=10**9
        sum+= tmp
    # print(sum)
    ans = min(ans, sum)
print(ans)
