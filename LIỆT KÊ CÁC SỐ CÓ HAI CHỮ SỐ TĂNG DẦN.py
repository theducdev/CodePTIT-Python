text = input()
a = set()
for i in range(0, len(text), 2):
    a.add(int(text[i:i+2]))
b = list(a)
b.sort()
for x in b:
    if x >=10:
        print(x, end = " ")
