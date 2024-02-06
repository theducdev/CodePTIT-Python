import math
for t in range(int(input())):
    num = input()
    check = 1
    for i in range (0, len(num), 2):
        if num[i] != num[0]:
            check = 0
            break
    if len(num)%2!=0 and num[0] != num[1] and check:
        print("YES")
    else:
        print("NO")