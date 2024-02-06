# from math import ceil
# class SinhVien:
#     def __init__(self, i, hoten, d1, d2, d3):
#         self.ma = f"SV{i:02d}"
#         self.hoten = ' '.join(hoten.title().split())
#         self.tb = (d1*3+d2*3+d3*2)/8
#
#     def __str__(self):
#         return "{} {} {:.2f} {}".format(self.ma, self.hoten, ceil(self.tb * 100) / 100, self.xh)
#
#
# n = int(input())
# ds = []
# for i in range(1, n+1):
#     hoten = input()
#     d1 = float(input())
#     d2 = float(input())
#     d3 = float(input())
#     ds.append(SinhVien(i, hoten, d1, d2, d3))
# ds.sort(key=lambda x: (-x.tb, x.ma))
# ds[0].xh = 1
# for i in range(1, n):
#     ds[i].xh = ds[i-1].xh if ds[i].tb == ds[i-1].tb else i+1
# print(*ds, sep = '\n')
#
#
#

