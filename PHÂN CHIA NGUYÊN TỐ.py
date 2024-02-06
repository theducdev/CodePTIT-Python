import math
def loaibotrungnhau(a):
    used = [0]*100005
    for x in a:
        used[x]+=1
    b =[]
    for x in a:
        if used[x] >=1:
            b.append(x)
            used[x] = 0
    return b


def checkSnt(n):
    if n <2: return False
    for i in range(2, int(math.sqrt(n)+1)):
        if n%i==0:
            return False
    return True


n = int(input())
a = []
while len(a) < n:
    for x in input().split():
        a.append(int(x))
sum = 0
b = loaibotrungnhau(a)
for x in b: sum+=x
tmp = 0
ans = -1
for i in range (len(b)):
    tmp+=b[i]
    if checkSnt(tmp) and checkSnt(sum-tmp):
        ans = i
        break
if ans==-1:
    print("NOT FOUND")
else:
    print(ans)

