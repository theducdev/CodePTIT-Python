
for t in range(int(input())):
    s = input()
    n = input()
    cnt = 0
    i = 0
    while i <= len(s)-len(n)+1:
        if s[i:i+len(n)] == n:
            cnt+=1
            i+=len(n)
        else:
            i+=1
    print(cnt)

    
