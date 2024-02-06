a = []
while len(a) < 10:
    a += [int(i)%42 for i in input().split()]
print(len(set(a)))
