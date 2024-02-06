from itertools import permutations
a = [x for x in input()]
ds = list(permutations(a))
for x in ds:
    print(*x, sep="")
