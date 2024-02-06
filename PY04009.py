class SoPhuc:
    def __init__(self, a, b):
        self.thuc = a
        self.ao = b

    def cong(self, a):
        return SoPhuc(self.thuc + a.thuc, self.ao + a.ao)

    def nhan(self, x):
        return SoPhuc(self.thuc*x.thuc - self.ao*x.ao, self.thuc*x.ao + self.ao*x.thuc)
    def __str__(self):
        if self.ao < 0: return "{} - {}i".format(self.thuc, -self.ao)
        return "{} + {}i".format(self.thuc, self.ao)

n = int(input())
for _ in range(n):
    a, b, c, d = [int(i) for i in input().split()]
    x = SoPhuc(a, b)
    y = SoPhuc(c, d)
    print(x.cong(y).nhan(x), end=", ")
    print(x.cong(y).nhan(x.cong(y)))



