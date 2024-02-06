import math

while True:
    line = input()
    if len(line.split())==1: break
    l, r = [int(i) for i in line.split()]
    n = int(input())
    tich = 1
    for x in range(2,n+1):
        tich=math.lcm(x,tich)
    cnt = 0
    i = 1
    while i*tich<=n:
        if i*tich >= l:
            cnt+=1
        i+=1
    print(cnt)
