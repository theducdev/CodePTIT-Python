import math
class Nv:
    def __init__(self,i, hoten, lt, th):
        self.ma = "TS0" + str(i)
        self.hoten = hoten
        tb = (lt+th)/2
        self.tb = float(tb)
        if tb < 5:
            x = "TRUOT"
        elif tb>=5 and tb<8:
            x = "CAN NHAC"
        elif tb >=8 and tb <=9.5:
            x = "DAT"
        else:
            x = "XUAT SAC"
        self.xl = x

    def __str__(self):
        return "{} {} {:.2f} {}".format(self.ma, self.hoten, self.tb, self.xl)

ds = []
for i in range(int(input())):
    hoten = input()
    d1 = float((input()))
    if d1>10: d1/=10
    d2 = float((input()))
    if d2>10: d2/=10
    ds.append(Nv(i+1, hoten, d1, d2))
ds.sort(key=lambda x : (-x.tb, x.ma))
print(*ds, sep='\n')
    

        