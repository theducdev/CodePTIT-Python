def Try(a, n, cuoicung, ds):
    if sum(a)==n:
        ds.append(a.copy())
    for i in range(min(n-sum(a), cuoicung), 0, -1):
        a.append(i)
        Try(a, n, i, ds)
        a.pop(len(a)-1)

for _ in range(int(input())):
    n = int(input())
    a = []
    ds = []
    Try(a, n, n, ds)
    print(len(ds))
    for x in ds:
        print('(', end = "")
        for i in range(len(x)):
            if i == len(x)-1:
                print(x[i], end = ') ')
            else:
                print(x[i], end = " ")
    print()
