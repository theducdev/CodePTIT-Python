def chuyen(s):
    return str(int(s[0])*4 + int(s[1])*2 + int(s[2]))

s = input()
if len(s)%3==1:
    s = '00' + s
elif len(s)%3==2:
    s = '0' + s
ans = ""

for i in range(0, len(s)-2, 3):
    ans+=chuyen(s[i:i+3])
print(ans)
