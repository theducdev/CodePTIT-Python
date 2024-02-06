n = int(input())
for i in range(1, n+1):
    print(f"Test {i}: ", end ="")
    s1 = [x for x in input()]
    s2 = [x for x in input()]
    s1.sort()
    s2.sort()
    if s1 == s2:
        print("YES")
    else: print("NO")
