def sang():
    f = [1]*1000000
    f[1] = 1
    f[2] = 1
    for i in range(2, 1000000):
        if f[i] == 1:
            for j in range(i*2, 1000000, i):
                f[j] = 0
    snt = []
    for i in range(2, 1000000):
        if f[i] ==1:
            snt.append(i)

    return snt


n, x = [int(i) for i in input().split()]
snt = sang()
print(x, end=" ")
tmp = x
for i in range(0, n):
    tmp+=snt[i]
    print(tmp, end = " ")


