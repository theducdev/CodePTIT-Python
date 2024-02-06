import math
class PhanSo:
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau
    def rutgon(self):
        x = math.gcd(self.tu, self.mau)
        tumoi = self.tu//x
        maumoi = self.mau//x
        return PhanSo(tumoi, maumoi)
    def toString(self):
        print(f"{self.tu}/{self.mau}")

    def cong(self, a):
        mau = self.mau * a.mau // math.gcd(self.mau, a.mau)
        res = PhanSo(self.tu * mau // self.mau + a.tu * mau // a.mau, mau)
        return res.rutgon()

tu1, mau1, tu2, mau2 = (int(i) for i in input().split())
p1 = PhanSo(tu1, mau1)
p2 = PhanSo(tu2, mau2)
p3 = p1.cong(p2)
print(f"{p3.tu}/{p3.mau}")
