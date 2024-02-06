class Khach:
    def __init__(self, i, ten, tong):
        self.ma =  f"KH{i:02d}"
        self.ten = ten
        self.tong = tong

    def __str__(self):
        return '{} {} {}'.format(self.ma, self.ten, round(self.tong))


n = int(input())
ds = []
for i in range(1, n+1):
    ten = input()
    cu = int(input())
    moi = int(input())
    so = moi - cu
    if so <= 50:
        tong = 102/100*so*100
    elif so <= 100:
        tong = 103/100*((so-50)*150 + 50*100)
    else:
        tong = 105/100* ((so-100)*200 + 50*150 + 50*100)
    ds.append(Khach(i, ten, tong))
    ds.sort(key = lambda x: (-x.tong))
print(*ds, sep='\n')



