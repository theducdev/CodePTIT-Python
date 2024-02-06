n = int(input())
ds = []
for _ in range(0, n):
    x = input()
    y, z = [int(i) for i in input().split()]
    ds.append(dict(name = x, sobai = y, sub = z))
ds_sorted = sorted(ds, key=lambda x: (-x['sobai'], x['sub'], x['name']))
for x in ds_sorted:
    for key, value in x.items():
        print(value, end = " ")
    print()
