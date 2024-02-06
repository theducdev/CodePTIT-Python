from itertools import permutations
for _ in range(int(input())):
    a = [i for i in range(1, int(input())+1)]
    ds = list(permutations(a))
    ds.sort(reverse=True)
    print(len(ds))
    for x in ds:
        print(*x, sep="", end=" ")
    print()
