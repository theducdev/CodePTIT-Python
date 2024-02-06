n = int(input())
cnt = 0
a = [int(i) for i in input().split()]
for i in range(len(a)-1):
    if a[i] != a[i+1]:
        cnt+=1
print(cnt)
