n, m = [int(i) for i in input().split()]
a = [[int(i) for i in input().split()] for _ in range(n)]
if n > m:
    cnt = n-m
    for i in range(n):
        if i%2==0 and cnt!=0:
            a[i][0] = -1
            cnt-=1
    for i in range(n):
        if a[i][0]!=-1:
            for j in range(m):
                print(a[i][j], end = " ")
            print()
else:
    cnt = m-n
    for j in range(m):
        if j%2==1 and cnt!=0:
            a[0][j] = -1
            cnt-=1
    for i in range(n):
        for j in range(m):
            if a[0][j]!=-1:
                print(a[i][j], end = " ")
        print()



