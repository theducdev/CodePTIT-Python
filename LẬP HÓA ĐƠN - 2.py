from datetime import datetime
class KhachHang:
    def __init__(self, i, ten, phong, songay, dv):
        self.ma = f"KH{i:02d}"
        self.ten = ten
        self.phong = phong
        self.songay = songay
        x = 25
        if phong[0] == '2': x = 34
        elif phong[0] == '3': x = 50
        elif phong[0] == '4': x = 80
        self.tien = x*songay + dv

    def __str__(self):
        return '{} {} {} {} {}'.format(self.ma, self.ten, self.phong, self.songay, self.tien )


n = int(input())
ds = []
for i in range(1, n+1):
    ten = input()
    phong = input()
    bd = datetime.strptime(input().strip(), "%d/%m/%Y")
    kt = datetime.strptime(input().strip(), "%d/%m/%Y")
    songay = (kt-bd).days + 1
    dv = int(input())
    ds.append(KhachHang(i, ten, phong, songay, dv))
ds.sort(key=lambda x: -x.tien)
print(*ds, sep='\n')

