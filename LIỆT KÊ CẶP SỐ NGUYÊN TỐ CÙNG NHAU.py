import math

n = int(input())
used = [0]*1000005
a = sorted(int(i) for i in input().split())
for i in range(n-1):
    for j in range(i+1, n):
        if math.gcd(a[i], a[j])==1:
            print(a[i], a[j])



