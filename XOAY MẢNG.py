def xoay(a,n, d):
    ans = a.copy()
    for i in range(n):
        ans[i] = a[abs(i+d)%n]
    return ans

for _ in range(int(input())):
    n, d = [int(i) for i in input().split()]
    a = [i for i in input().split()]
    print(*xoay(a,n,d), sep=' ')
