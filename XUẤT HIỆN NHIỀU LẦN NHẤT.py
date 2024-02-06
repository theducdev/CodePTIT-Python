for _ in range(int(input())):
    n = int(input())
    used = [0]*1000005
    a = [int(i) for i in input().split()]
    Max = 0
    for x in a:
        used[x]+=1
        Max = max(Max, used[x])
    a.sort()
    if Max <= int(n/2):
        print("NO")
    else:
        for x in a:
            if used[x] == Max:
                print(x)
                break
