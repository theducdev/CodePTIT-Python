ds = []
ans = set()

f = open("CONTACT.in", "r")
for x in f:
    ans.add(x.strip().lower())
ds = [i for i in ans]
ds.sort()
print(*ds, sep='\n')


