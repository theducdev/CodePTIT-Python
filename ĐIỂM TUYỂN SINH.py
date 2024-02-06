class ThiSinh:
    def __init__(self, i, hoten, diem, dantoc, khuvuc):
        self.ma = f"TS{i:02d}"
        self.hoten = hoten
        uu = 0
        if not dantoc=="Kinh":
            uu+=1.5
        if khuvuc =="1":
            uu+= 1.5
        elif khuvuc =="2":
            uu+= 1

        self.diem = diem+uu
        if diem+uu>= 20.5: self.tt = "Do"
        else: self.tt = "Truot"

    def __str__(self):
        return "{} {} {} {}".format(self.ma,' '.join(self.hoten.title().split()), self.diem.__format__(".1f"), self.tt)


n = int(input())
ds = []
for i in range(1, n+1):
    hoten = input()
    diem = float(input())
    dantoc = input()
    khuvuc = input()
    ds.append(ThiSinh(i, hoten, diem, dantoc, khuvuc))

ds.sort(key=lambda x :(-x.diem, x.ma))

for x in ds:
    print(x)



