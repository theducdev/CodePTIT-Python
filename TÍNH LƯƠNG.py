class NhanVien:
    def __init__(self, ma, ten, coban, ngay ,phong ):
        self.ma = ma 
        self.ten = ten
        nhom = ma[0]
        nam = int(ma[1:3])
        self.phong = phong
        self.luong = coban*ngay*heso(nhom, nam)*1000

    def __str__(self):
        return "{} {} {}{}".format(self.ma, self.ten, self.phong, self.luong)


def heso(nhom, nam):
    x = 0
    if nhom == 'A':
        if nam >= 1 and nam <=3: x = 10 
        if nam >= 4 and nam <=8: x = 12 
        if nam >= 9 and nam <=15: x = 14 
        if nam >= 16: x = 20 
    if nhom == 'B':
        if nam >= 1 and nam <=3: x = 10 
        if nam >= 4 and nam <=8: x = 11 
        if nam >= 9 and nam <=15: x = 13 
        if nam >= 16: x = 26
    if nhom == 'C':
        if nam >= 1 and nam <=3: x = 9
        if nam >= 4 and nam <=8: x = 10 
        if nam >= 9 and nam <=15: x = 12 
        if nam >= 16: x = 14
    if nhom == 'D':
        if nam >= 1 and nam <=3: x = 8 
        if nam >= 4 and nam <=8: x = 9 
        if nam >= 9 and nam <=15: x = 11 
        if nam >= 16: x = 13
    return x



phong = {}
for _ in range (int(input())):
    line = input().split()
    tmp = ''
    for i in range(1,len(line)):
        tmp+=line[i]+" "
    phong[line[0]] = tmp
ds = []
for _ in range(int(input())):
    ma = input()
    ten = input()
    coban = int(input())
    ngay = int(input())
    ds.append(NhanVien(ma, ten, coban, ngay, phong[ma[3::]]))
print(*ds, sep ='\n')