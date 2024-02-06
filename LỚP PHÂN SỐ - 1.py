import math


class PhanSo:
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau
    def rutgon(self):
        x = math.gcd(self.tu, self.mau)
        tumoi = self.tu//x
        maumoi = self.mau//x
        print(f"{tumoi}/{maumoi}")

tu, mau = [int(i) for i in input().split()]
p = PhanSo(tu, mau)
p.rutgon()
