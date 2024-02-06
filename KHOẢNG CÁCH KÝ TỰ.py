def check(s):
    dao = s[::-1]
    for i in range(1, len(s)):
        if abs(ord(s[i]) - ord(s[i-1])) != abs(abs(ord(dao[i]) - ord(dao[i-1])) ): return False

    return True

for _ in range(int(input())):
    s = input()
    if check(s): print("YES")
    else: print("NO")
