from itertools import combinations
import re
n, k = [int(x) for x in input().split()]
ds = set(re.split(r'\s+', input()))
z = sorted(x for x in ds)
ans = list(combinations(z, k))
for x in ans:
    print(*x,sep=" ", end = '\n')

