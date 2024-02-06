mod = 10**9+7
for _ in range(int(input())):
    n, k = [int(i) for i in input().split()]
    k = bin(k)[2::][::-1]
    sum = 0
    ds = []
    for i in range(len(k)):
        sum+=int(k[i])*(n**i)%mod
    print(sum%mod)
