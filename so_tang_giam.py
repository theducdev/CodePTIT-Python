for t in range(int(input())):
    num = input()
    up = True
    check = 1
    if len(num) < 3: check = 0
    for i in range(1, len(num)):
        if up and num[i] <= num[i-1]:
            up = False
        elif not up and num[i] >= num[i-1]:
            check = 0
            break
    if check == 1:
        print("YES")
    else:
        print("NO")


