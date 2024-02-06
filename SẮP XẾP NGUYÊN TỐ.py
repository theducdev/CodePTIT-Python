import math


def checkSnt(n):
    if n <2: return False
    for i in range(2, int(math.sqrt(n)+1)):
        if n%i==0:
            return False
    return True


n = int(input())
a = [int(i) for i in input().split()]
tapSnt = [x for x in a if checkSnt(x)]

tapSnt.sort()
ans = []
idx = 0
for i in range(n):
    if checkSnt(a[i]):
        ans.append(tapSnt[idx])
        idx+=1
    else:
        ans.append(a[i])

for x in ans:
    print(x, end = " ")
print()
