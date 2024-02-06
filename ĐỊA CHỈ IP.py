def check(a):
    if len(a) < 4: return False
    for x in a:
        if x.isdigit():
            if int(x)<0 or int(x) >255:
                return False
        else: return False
    return True

for _ in range(int(input())):
    a = [x for x in input().split(".")]
    if check(a):
        print("YES")
    else:
        print("NO")

