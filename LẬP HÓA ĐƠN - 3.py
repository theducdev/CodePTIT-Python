class HoaDon:
    def __init__(self,ma, ten, mua, gia, chiet ):
        self.ma = ma
        self.ten = ten
        self.mua = mua
        self.gia = gia
        self.chiet = chiet
        self.tong = mua*gia - chiet

    def __str__(self):
        return '{} {} {} {} {} {}'.format(self.ma, self.ten, self.mua, self. gia, self.chiet, self.tong)

n = int(input())
ds = []
for _ in range(n):
    ma = input()
    ten = input()
    mua = int(input())
    gia = int(input())
    chiet = int(input())
    ds.append(HoaDon(ma, ten, mua, gia, chiet))
ds.sort(key = lambda x : -x.tong)
print(*ds, sep='\n')
