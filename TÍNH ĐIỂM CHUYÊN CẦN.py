class Hs:
    def __init__(self, ma, ten, lop, diem):
        self.ma = ma;
        self.ten = ten;
        self.lop = lop;
        self.diem = diem;

    def __str__(self):
        if self.diem == 0:  return '{} {} {} {} KDDK'.format(self.ma, self.ten, self.lop, self.diem)
        return '{} {} {} {}'.format(self.ma, self.ten, self.lop, self.diem)

n = int(input())
ds = []
for _ in range(n):
    ma = input()
    ten = input()
    lop = input()
    diem = 10
    ds.append(Hs(ma, ten, lop, diem))
for _ in range(n):
    ma, dd = [i for i in input().split(" ")]
    for j in ds:
        if (j.ma == ma):
            for k in dd:
                if k == 'm':
                    j.diem-=1
                elif k == 'v':
                    j.diem -=2
        if j.diem < 0: j.diem = 0

print(*ds, sep='\n')

