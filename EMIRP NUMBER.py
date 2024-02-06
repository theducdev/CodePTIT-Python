f = [0] * 1000005
f[0] = 1
f[1] = 1
for i in range(2, 1000005):
    if f[i] == 0:
        for j in range(i * i, 1000005, i):
            f[j] = 1


def is_valid(n):
    is_valid_check = 1
    if f[int(n)] != 0:
        is_valid_check = 0
    if f[int(n[::-1])] != 0:
        is_valid_check = 0
    if (int(n)==int(n[::-1])): is_valid_check = 0
    return is_valid_check

for _ in range(int(input())):
    n = int(input())
    for i in range(1, n+1):
        if is_valid(str(i)) and int(str(i)[::-1]) <= n and i < int(str(i)[::-1]):
            print(i, str(i)[::-1] , end = " ")
    print()

