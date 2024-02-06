class Ts:
    def __init__(self, ten, donvi, kt):
        self.ten = ten
        self.donvi = donvi
        a = [x for x in ten.split(" ")]
        b = [x for x in donvi.split(" ")]
        z = ""
        for x in b:
            z+=x[0]
        for x in a:
            z+=x[0]
        self.ma = z;
        self.vantoc = 120/((tinhPhut(kt) - tinhPhut("6:00"))/60)

    def __str__(self):
        return '{} {} {} {} Km/h'.format(self.ma, self.ten, self.donvi, round(self.vantoc))


def tinhPhut(x):
    gio, phut = [int(i) for i in x.split(":")]
    return gio*60+phut

n = int(input())
ds = []
for _ in range(n):
    ds.append(Ts(input(), input(), input()))
ds.sort(key=lambda x: -x.vantoc)
print(*ds, sep='\n')
