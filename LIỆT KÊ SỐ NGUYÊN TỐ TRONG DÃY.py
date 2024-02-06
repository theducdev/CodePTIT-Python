import math
def checkSnt(x):
    if x < 2: return False
    for i in range(2, int(math.sqrt(x)+1)):
        if x%i==0:
            return False
    return True


n = int(input())
a = [int(i) for i in input().split()]
used = [0]*1000000
for x in a:
    used[x]+=1
for x in a:
    if checkSnt(x) and used[x]:
        print(x, used[x])
        used[x]=0






