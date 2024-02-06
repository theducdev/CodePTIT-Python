def solve(a):
    ans = ""
    for i in range(0, n):
        if i%2==0:
            for x in a[i]:
                ans+= f"{x} "
        else:
            for x in a[1][::-1]:
                ans+=f"{x} "
    return ans



for _ in range(int(input())):
    n = int(input())
    line = [int(x) for x in input().split()]
    a = []*n
    for i in range(0, n*n-1, n):
        b = []
        for j in range(0,n):
            b.append(line[i+j])
        a.append(b.copy())
    print(solve(a))

