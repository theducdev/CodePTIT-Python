so = input()
cnt = 0
for i in range (0, len(so)):
    if so[i] == '4' or so[i] == '7':
        cnt+=1
if (cnt == 4 or cnt == 7):
    print("YES")
else:
    print("NO")
