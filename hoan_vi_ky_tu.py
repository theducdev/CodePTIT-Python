def Try(l, n, used):
    if len(l) == n:
        for i in range (1, n+1):
            print(text[l[i-1]-1], end="")
        print()
        return
    for j in range(1, n+1):
        if used[j] == 0:
            used[j] = 1
            l.append(j)
            Try(l, n, used)
            used[j] = 0
            l.pop()


text = input()
used = [0] * (len(text)+1)
Try([], len(text),used)


