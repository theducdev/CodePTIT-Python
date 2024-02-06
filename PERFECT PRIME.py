f = [0] * 100000005
f[0] = 1
f[1] = 1
for i in range(2, 100000005):
    if f[i] == 0:
        for j in range(i * i, 100000005, i):
            f[j] = 1


def is_valid(n):
    is_valid_check = 1
    if f[int(n)] != 0:
        is_valid_check = 0
    if f[int(n[::-1])] != 0:
        is_valid_check = 0
    SUM = 0
    for x in n:
        if f[int(x)] != 0:
            is_valid_check = 0
            break
        SUM += int(x)
    if f[SUM] != 0:
        is_valid_check = 0
    return is_valid_check


t = int(input())
while t > 0:
    n = input()
    if is_valid(n):
        print("Yes")
    else:
        print("No")
    t -= 1
