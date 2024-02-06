for _ in range(int(input())):
    sum = 0
    str = []
    s = input()
    for x in s:
        if x.isdigit():
            sum+=int(x)
        else:
            str.append(x)
    str.sort()
    for x in str:
        print(x, end="")
    print(sum)
