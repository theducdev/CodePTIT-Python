from collections import deque

v = []
n = int(input())
tmp = "2357"
def check(s):
    z = set(s)
    if len(z)!=4: return False
    elif s[-1]=="2": return False
    return True
def gen():
    q = deque()
    for x in tmp: q.append(x)
    while True:
        p=q.popleft()
        if len(p) == n: break
        for x in tmp:
            tmp1=p+x
            q.append(tmp1)
            if check(tmp1): v.append(tmp1)
gen()
for x in v:
    print(x)
