n = int(input())
used = [0]*1000005
a = [int(i) for i in input().split()]
for x in a:
    used[x]+=1
ans = n+1
for i in range(1, n+1):
    if used[i]==0:
        ans = i
        break
print(ans)
