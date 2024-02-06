P = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
while True:
    inputs = input().split()
    k = int(inputs[0])
    if k == 0:
        break
    s = inputs[1]
    ans = ""
    for i in range (len(s)):
        ans = P[(P.find(s[i])+k)%28] + ans
    print(ans)
    
