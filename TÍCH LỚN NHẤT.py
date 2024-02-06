def tinh(a, n):
    b = []
    a.sort()
    b.append(a[0]*a[1])
    b.append(a[-1]*a[-2])
    b.append(a[-1]*a[-2]*a[-3])
    b.append(a[0]*a[1]*a[-1])
    b.sort()
    return b[-1]

n = int(input())
a = [int(i) for i in input().split()]
print(tinh(a,n))
