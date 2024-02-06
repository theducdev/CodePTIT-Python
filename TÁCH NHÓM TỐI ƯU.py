n, k = [int(i) for i in input().split()]
a = sorted([int(i) for i in input().split()])
cnt = 1
for i in range(0, n-1):
    if abs(a[i]-a[i+1]) > k:
        cnt+=1
print(cnt)
