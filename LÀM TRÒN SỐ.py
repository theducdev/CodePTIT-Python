for _ in range(int(input())):
    a = [int(i) for i in input()]
    for i in range(len(a)-1, 0, -1):
        if a[i] >=5:
            a[i-1]+=1
        a[i] = 0
    print(*a, sep="")

