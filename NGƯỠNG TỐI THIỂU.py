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
a = list()
for i in range(0, len(text), 2):
    a.append(int(text[i:i+2]))
b = loaibotrungnhau(a)
for x in b:
    if x >=10:
        print(x, end = " ")
