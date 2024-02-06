for _ in range(int(input())):
    ds = dict()
    line = input()
    if len(line) >100:
        ans = [line[i] for i in range(0,101)]
        while ans[-1].isalpha():
            ans.pop(-1)
    else:
        ans = [line[i] for i in range(len(line))]
    print(*ans, sep = "")
