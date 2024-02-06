def loaibotrungnhau(a):
    used = [0]*100005
    for x in a:
        used[x]+=1
    b =[]
    for x in a:
        if used[x] >=1:
            b.append(x)
            used[x] = 0
    return b


text = input()
k = int(input())
a = list()
for i in range(0, len(text), 2):
    a.append(int(text[i:i+2]))
used = [0]*100005
for x in a:
    used[x]+=1
check = 0
a.sort()
for x in a:
    if x >=10 and used[x] >=k:
        print(x,used[x])
        check = 1
        used[x] = 0
if check ==0:
    print("NOT FOUND")
