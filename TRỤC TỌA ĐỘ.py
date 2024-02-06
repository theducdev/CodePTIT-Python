class Doan:
    def __init__(self, dau, cuoi):
        self.dau = dau
        self.cuoi = cuoi

for _ in range(int(input())):
    ds = []
    n = int(input())
    for _ in range(n):
        dau, cuoi = [int(i) for i in input().split()]
        ds.append(Doan(dau, cuoi))
    ds.sort(key=lambda x: (x.cuoi))
    tmp = ds[0].cuoi
    cnt = 1
    for i in range(1, n):
        if ds[i].dau>=tmp:
            cnt+=1
            tmp = ds[i].cuoi
    print(cnt)
