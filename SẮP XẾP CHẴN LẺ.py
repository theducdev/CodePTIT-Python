n = int(input())
a = []
while len(a) < n:
    for x in input().split():
        a.append(int(x))
check = [i%2==0 for i in a]
chan = []
le = []
for x in a:
    if x%2==0:
        chan.append(x)
    else:
        le.append(x)
chan.sort()
le.sort(reverse=True)
ans = []
chanidx = leidx = 0
for i in range(n):
    if check[i]:
        ans.append(chan[chanidx])
        chanidx+=1
    else:
        ans.append(le[leidx])
        leidx+=1
for x in ans:
    print(x, end = " ")
print()
