class Gamer:
    def __init__(self, ma, ten, bd, kt):
        self.ma = ma;
        self.ten = ten;
        phutt = self.tinhPhut(kt) - self.tinhPhut(bd)
        self.sophut = phutt
        self.gio = phutt//60
        self.phut = phutt%60


    def tinhPhut(self, x):
        gio, phut = [int(i) for i in x.split(":")]
        return gio*60+phut


    def __str__(self):
        return '{} {} {} gio {} phut '.format(self.ma, self.ten, self.gio, self.phut);


n = int(input())
ds = []
for _ in range(n):
    ma = input()
    ten = input()
    bd = input()
    kt = input()
    ds.append(Gamer(ma, ten, bd, kt))
ds.sort(key=lambda x: -x.sophut)
print(*ds, sep='\n')
