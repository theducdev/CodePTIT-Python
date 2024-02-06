for _ in range(int(input())):
    n = int(input())
    check = 1
    a = sorted(int(i) for i in input().split())
    b = sorted(int(i) for i in input().split())
    for i in range(len(a)):
        if a[i] > b[i]:
            check = 0
            break
    if check:
        print("YES")
    else:
        print("NO")
