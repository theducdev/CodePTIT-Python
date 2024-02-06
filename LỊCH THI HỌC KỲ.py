from datetime import datetime

class Lich:
    def __init__(self,i, mamon, ngay, gio, nhom, tenmon):
        self.macathi = f"T{i:03d}"
        self.mamon = mamon
        self.ngay = datetime.strptime(ngay, "%d/%m/%Y")
        self.gio = datetime.strptime(gio, "%H:%M")
        self.nhom = nhom
        self.tenmon = tenmon


    def __str__(self):
        return "{} {} {} {} {} {}".format(self.macathi, self.mamon, self.tenmon, self.ngay.strftime("%d/%m/%Y"), self.gio.strftime("%H:%M"), self.nhom)


n, m = [int(i) for i in input().split()]
dsMon = dict()
for _ in range(n):
    mamon = input()
    tenmon = input()
    dsMon[mamon] = tenmon


dsLich = []
for i in range(1, m+1):
    mamon, ngay, gio, nhom = [x for x in input().split()]
    dsLich.append(Lich(i, mamon, ngay, gio, nhom, dsMon[mamon]))

dsLich.sort(key=lambda x : (x.ngay, x.gio, x.mamon))

for x in dsLich:
    print(x)



