class Nguoi:
    def __init__(self, ten, sdt, ngay):
        self.ten = ten
        self.sdt = sdt
        self.ngay = ngay

    def __str__(self):
        return "{}: {} {}".format(self.ten, self.sdt, self.ngay)

f = open("SOTAY.txt", "r")
ds = f.read().split('\n')
dsSdt = []
used = []
for x in ds:
    tmp = x.split(' ')
    if tmp[0] == "Ngay" and len(tmp)==2:
        used.append(1)
    else:
        used.append(0)
i = 0
ngay = ''
while i < len(ds)-1:
    if used[i] == 1:
        ngay = ds[i].split(' ')[1]
    else:
        ten = ds[i]
        i+=1
        sdt = ds[i]
        dsSdt.append(Nguoi(ten, sdt, ngay))
    i+=1
dsSdt.sort(key=lambda x : x.ngay)
f.close()
out = open("DIENTHOAI.txt", "w")
for x in dsSdt: out.write(x.__str__() + '\n')
out.close()



