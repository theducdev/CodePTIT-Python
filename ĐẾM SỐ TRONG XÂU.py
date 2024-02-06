for _ in range(int(input())):
    text = input()
    target = input()
    cnt = 0
    i = 0
    while i < len(text):
        if text[i:i+len(target)] == target:
            cnt += 1
            i += len(target)
        else:
            i += 1
    print(cnt)
