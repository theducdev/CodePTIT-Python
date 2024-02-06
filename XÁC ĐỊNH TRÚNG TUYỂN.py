class GiaoVien:
    def __init__(self, i, ten, maxt, tin, cm):
        self.ma = f"GV{i:02d}"
        self.ten = ten
        uu = 0
        if maxt[1] == '1': uu = 2
        elif maxt[1] == '2': uu = 1.5
        elif maxt[1] == '3': uu = 1

        if maxt[0] == 'A': self.mon= "TOAN"
        elif maxt[0] == 'B': self.mon = "LY"
        elif maxt[0] == 'C': self.mon = "HOA"
        self.tong = uu + tin*2 + cm
        if self.tong >= 18: self.kq = "TRUNG TUYEN"
        else: self.kq = "LOAI"

    def __str__(self):
        return '{} {} {} {} {}'.format(self.ma, self.ten, self.mon, self.tong, self.kq)


n = int(input())
ds = []
for i in range(1, n+1):
    ten = input()
    maxt = input()
    tin = float(input())
    cm = float(input())
    ds.append(GiaoVien(i, ten, maxt, tin, cm))

ds.sort(key= lambda x : -x.tong)
print(*ds, sep='\n')
