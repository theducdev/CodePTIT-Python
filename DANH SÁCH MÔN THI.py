class Mon:
    def __init__(self, ma, ten, ht):
        self.ma = ma
        self.ten = ten
        self.ht = ht

    def __str__(self):
        return "{} {} {}".format(self.ma, self.ten, self.ht)

ds = []
for _ in range(int(input())):
    ma = input()
    ten = input()
    ht = input()
    ds.append(Mon(ma, ten, ht))
ds.sort(key=lambda x : (x.ma))
print(*ds, sep='\n')
        