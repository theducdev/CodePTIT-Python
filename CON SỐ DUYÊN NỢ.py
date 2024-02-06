def check(s):
    if s[0] == s[len(s)-1]: return True
    return False


for _ in range(int(input())):
    s = input()
    if check(s): print("YES")
    else: print("NO")
