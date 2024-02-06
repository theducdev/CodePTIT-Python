for _ in range(int(input())):
    n = int(input())
    used = [0]*1001
    a = []
    Max = 0
    for _ in range(n):
        x = int(input())
        a.append(x)
        used[x]+=1
        Max = max(Max, used[x])
    a.sort()
    for x in a:
        if used[x] == Max:
            print(x)
            break
