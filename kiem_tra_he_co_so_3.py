for t in range(int(input())):
    num = input()
    check = 1
    for i in range(0, len(num)):
        if num[i] != '1' and num[i] != '0' and num[i] != '2':
            check = 0
            break
    if check == 1:
        print("YES")
    else:
        print("NO")


