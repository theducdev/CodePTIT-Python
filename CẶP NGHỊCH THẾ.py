n = int(input())
cnt = 0
a = [int(i) for i in input().split()]
for i in range(len(a)-1):
    for j in range(i+1, len(a)):
        if a[i] > a[j]:
            cnt+=1
print(cnt)
