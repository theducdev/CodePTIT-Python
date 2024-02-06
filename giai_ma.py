for t in range(int(input())):
    code = input()
    ans = ""
    for i in range(len(code)):
        if(i%2==1):
            for j in range (int(code[i])):
                ans+=code[i-1]


    print(ans)
