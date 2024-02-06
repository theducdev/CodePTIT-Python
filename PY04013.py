from collections import defaultdict
def chuyenSangPhut(batdau):
    gio, phut = map(int, batdau.split(":"))
    return gio*60 + phut

def tinhToan(dslando):
    cactram = defaultdict(lambda: {"luongmua":0, "sophut":0} )
    for do in dslando:
        tentram, batdau, ketthuc, luongmua = do
        thoigian = chuyenSangPhut(ketthuc) - chuyenSangPhut(batdau)

        cactram[tentram]["luongmua"]+=luongmua
        cactram[tentram]["sophut"]+=thoigian

    for i, (tentram, data) in enumerate(cactram.items(), start=1):
        tb = data["luongmua"]/data["sophut"]*60
        print(f"T{i:02d} {tentram} {tb:.2f}")


n = int(input())
dsdo = []
for _ in range(n):
    tentram = input()
    batdau = input()
    ketthuc = input()
    luongmua = float(input())
    dsdo.append((tentram, batdau, ketthuc, luongmua))

tinhToan(dsdo)





