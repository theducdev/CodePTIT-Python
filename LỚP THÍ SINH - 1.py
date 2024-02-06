class ThiSinh:
    def __init__(self, hoten, ns, d1, d2, d3):
        self.hoten = hoten
        self.ns = ns
        self.d1 = d1
        self.d2 = d2
        self.d3 = d3

    def toString(self):
        return self.hoten + " " + self.ns + " " + "{:.1f}".format(self.d1 + self.d2 + self.d3)


hoten = input()
ns = input()
d1 = float(input())
d2 = float(input())
d3 = float(input())
x = ThiSinh(hoten, ns, d1, d2, d3)
print(x.toString())
