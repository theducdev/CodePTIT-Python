f = [0]*101
def dp(n, x, y, z):
    f[1] = x
    for i in range(2, n+1):
        if i%2==0:
            f[i] = min(f[i-1]+x, f[i//2]+z)
        else:
            f[i] = min(min(f[i-1]+x, f[(i-1)//2]+x + z), f[(i+1)//2] +z+ y )
    return f[n]

for _ in range(int(input())):
    n = int(input())
    x,y,z = [int(i) for i in input().split()]
    print(dp(n,x,y,z))
