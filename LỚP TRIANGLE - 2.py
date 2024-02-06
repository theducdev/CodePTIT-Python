import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance(p1, p2):
        return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)


class Triangle:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def chuvi(self):
        a = Point.distance(self.p1, self.p2)
        b = Point.distance(self.p3, self.p2)
        c = Point.distance(self.p1, self.p3)
        if a+b <= c or a+c <= b or b+c<= a:
            print("INVALID")
        else:
            print("{:.3f}".format(a+b+c))

    def dientich(self):
        a = Point.distance(self.p1, self.p2)
        b = Point.distance(self.p3, self.p2)
        c = Point.distance(self.p1, self.p3)
        if a+b <= c or a+c <= b or b+c<= a:
            print("INVALID")
        else:

            print('{:.2f}'.format(math.sqrt((a + b + c) * (a + b - c) * (a - b + c) * (-a + b + c)) / 4))


a=[]
t=int(input())
for x in range(t):
    a+=[float(i) for i in input().split()]
i=0
for index in range(t):
    tri=Triangle(Point(a[i],a[i+1]),Point(a[i+2],a[i+3]),Point(a[i+4],a[i+5]))
    tri.dientich()
    i+=6
