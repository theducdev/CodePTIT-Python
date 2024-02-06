for t in range (int(input())):
    num = input()
    check = 1
    for i in range(len(num)-1):
        if int(num[i]) > int(num[i+1]):
            check = 0
            break
    if check:
        print("YES")
    else:
        print("NO")