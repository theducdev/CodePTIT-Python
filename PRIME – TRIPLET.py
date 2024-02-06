f = [1]*1000005
f[0] = 0
f[1] = 0
for i in range(2, 1000005):
    if f[i]==1:
        for j in range(i*i, 1000005, i):
            f[j]=0

def check1(n):
    if f[n] and f[n+2] and f[n+6]: return True
    return False


def check2(n):
    if f[n] and f[n+4] and f[n+6]: return True
    return False



for _ in range(int(input())):
    n = int(input())
    cnt = 0
    for i in range(2, n+1-6):
        if check1(i):
            cnt+=1
        if check2(i):
            cnt+=1
    print(cnt)
