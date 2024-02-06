def check(a):
    if a==a[::-1]: return True
    return False
ds = dict()
f = open("VANBAN.in", "r")
for x in f:
    for i in x.strip().split(' '):
        if check(i):
            if i in ds: ds[i]['xuathien']+=1
            else: ds[i] = {'dodai': len(i), 'xuathien': 1}
ans = sorted(ds.items(), key = lambda x : -x[1]['dodai'])
Max = ans[0][1]['dodai']
for x in ds:
    if ds[x]['dodai'] == Max:
        print(x, ds[x]['xuathien'])


