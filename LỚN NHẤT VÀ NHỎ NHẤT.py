def Min_Max(a):
    a.sort()
    if a[0] == a[-1]:
        print("BANG NHAU")
    else:
        print(a[0], a[-1])


while True:
    n = int(input())
    if n==0: break
    a = []
    for _ in range(n):
        a.append(int(input()))
    Min_Max(a)


