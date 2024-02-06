t = int(input())
while t:
    so = input()
    cnt = 0
    check = 1
    for i in range (0, len(so)):
        if so[i] != '4' and so[i] != '7':
            check = 0
            break
    if (check == 1):
        print("YES")
    else:
        print("NO")
    t-=1
