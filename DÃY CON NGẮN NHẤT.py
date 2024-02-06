import math

for _ in range(int(input())):
    a = []
    n, k = [int(i) for i in input().split()]
    a =[int(i) for i in input().split()]
    f = a.copy()
    ans = 1
    i = 1
    while i < n:
        GCD = math.gcd(f[i-1], a[i])
        if GCD==k:
            f[i-1] = k
            i+=1
        elif GCD < k:
            i+=2
        else:
            f[i-1] = GCD
            f[i] = GCD
            i+=1
    print(*f, sep=" ")



