f = [0]*93
f[1] = 1
f[2] = 1
for i in range(3, 93):
    f[i] = f[i-1] + f[i-2]

for _ in range(int(input())):
    a, b = [int(i) for i in input().split()]
    for i in range(a, b+1):
        print(f[i], end=" ")
    print()
