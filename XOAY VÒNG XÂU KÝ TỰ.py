n =int(input())
ds = []
ok = 1
for i in range(n):
    ds.append(input())
s = ds[0]
ans = 10**9
for i in range(len(s)):
    tmp = 0
    for j in range(n):
        ds1 = ds.copy()
        cnt = 0
        while ds1[j] != s:
            ds1[j] = ds1[j][1::] + ds1[j][0]
            cnt+=1
            if cnt == len(s):
                ok = 0
                break
        tmp+=cnt
    ans = min(ans, tmp)
    s = s[1::] + s[0]
print(ans) if ok == 1 else print(-1)
