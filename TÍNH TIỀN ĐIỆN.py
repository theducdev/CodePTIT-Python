class Gd:
    def __init__(self, i, ten, loaiho, dau, cuoi):
        self.ma = f"KH{i:02d}"
        self.ten = chuanHoa(ten)
        dinhmuc = 200
        if loaiho =='A': dinhmuc = 100
        elif loaiho == 'B': dinhmuc = 500
        trong = 0
        vuot = 0
        sodien = cuoi-dau
        if sodien < dinhmuc:
            trong = sodien*450
        elif sodien>=dinhmuc:
            trong = dinhmuc*450
            vuot = (sodien-dinhmuc)*1000
        self.vuot = (vuot)
        self.trong = (trong)
        self.thue = (vuot//20)
        self.tong = (trong + vuot + self.thue)

    def __str__(self):
        return "{} {}{} {} {} {}".format(self.ma, self.ten, self.trong, self.vuot, self.thue, self.tong)

def chuanHoa(line):
    a = line.strip().split()
    ten = ''
    for x in a:
        ten+=x.title() + ' '
    return ten


ds = []
for i in range(int(input())):
    ten = input()
    line = input().split()
    loaiho = line[0]
    dau = int(line[1])
    cuoi = int(line[2])
    ds.append(Gd(i+1, ten, loaiho, dau, cuoi))
ds.sort(key= lambda x : -x.tong)
print(*ds, sep='\n')

