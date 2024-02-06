for t in range(int(input())):
    code = input()
    ans = ""
    cnt = 1
    for i in range(len(code)-1):
        if code[i] == code[i+1]:
            cnt+=1
        else:
            ans+=str(cnt)
            ans+=code[i]
            cnt = 1
    ans+=str(cnt)
    ans+=code[len(code)-1]
    print(ans)
