def check(n, i):
    if i%2==0:
        return 1 if (n-i/2)/i==int((n-i/2)/i) and tinha(n,i) else 0
    return 1 if n/i == int(n/i) and tinha(n,i) else 0

def tinha(n, i):
    if i%2 ==0:
        a = (n-i/2)/i
        return 1 if a >= i/2 else 0
    a = n/i
    return 1 if a >= (i-1)/2+1 else 0

for _ in range(int(input())):
    n = int(input())
    cnt = 0
    for i in range(2, 50000):
        if check(n, i):
            cnt+=1
    print(cnt)

