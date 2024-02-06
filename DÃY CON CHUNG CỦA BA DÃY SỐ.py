for _ in range(int(input())):
    n, m, k = [int(i) for i in input().split()]
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    c = [int(i) for i in input().split()]
    giao = []
    i = j = l = 0
    while i < n and j < m and l < k:
        if a[i] == b[j] and b[j] == c[l]:
            giao.append(a[i])
            i+=1
            j+=1
            l+=1
        elif a[i] <= b[j] and a[i] <= c[l]:
            i+=1
        elif b[j] <= c[l] and b[j] <= a[i]:
            j+=1
        elif c[l] <= a[i] and c[l] <= b[j]:
            l+=1
    if len(giao)==0:
        print("NO")
    else:
        for x in giao:
            print(x, end = " ")
    print()
