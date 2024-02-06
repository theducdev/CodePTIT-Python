def biendoi(a):
    x = a[0]
    for i in range(0,3):
        a[i] = abs(a[i]-a[i+1])
    a[3] = abs(a[3]-x)


while True:
    a = [int(i) for i in input().split()]
    if a[0] == 0 and a[1] == 0 and a[2] == 0 and a[3] == 0: break
    cnt = 0
    while len(set(a))!=1:
        cnt+=1
        biendoi(a)
    print(cnt)
