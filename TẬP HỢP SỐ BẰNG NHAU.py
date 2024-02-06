n, m = [int(i) for i in input().split()]
a = list(set(int(i) for i in input().split()))
b = list(set(int(i) for i in input().split()))
giao = []
i = j = 0
while i < len(a) and j < len(b):
    if a[i] == b[j]:
        giao.append(a[i])
        i += 1
        j += 1
    elif a[i] < b[j]:
        i += 1
    else:
        j += 1
if len(giao)==len(a) and len(giao)==len(b):
    print("YES")
else:
    print("NO")
