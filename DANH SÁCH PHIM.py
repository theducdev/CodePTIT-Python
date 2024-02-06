from datetime import datetime
class Phim:
    def __init__(self, i, matheloai, ngay, tenphim, tap, tentheloai):
        self.maphim = f"P{i:03d}"
        self.tenphim = tenphim
        self.ngay = datetime.strptime(ngay, "%d/%m/%Y")
        self.tap = tap
        self.matheloai = matheloai
        self.tentheloai = tentheloai


    def __str__(self):
        return "{} {} {} {} {}".format(self.maphim, self.tentheloai, self.ngay.strftime("%d/%m/%Y"), self.tenphim, self.tap)



dstl = dict()
dsPhim = []
n, m = [int(i) for i in input().split()]
for i in range(1, n+1):
    matheloai = f"TL{i:03d}"
    dstl[matheloai] = input()

for i in range(1, m+1):
    matheloai = input()
    ngay = input()
    tenphim = input()
    tap = int(input())
    dsPhim.append(Phim(i, matheloai,ngay, tenphim, tap, dstl[matheloai]))


dsPhim.sort(key = lambda x : (x.ngay, x.tenphim, -x.tap) )

for x in dsPhim:
    print(x, sep='\n')
