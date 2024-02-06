class ThiSinh:
    def __init__(self, i, tenthisinh, tenteam, tentruong):
        self.mathisinh = f"C{i:03d}"
        self.tenthisinh = tenthisinh
        self.tenteam = tenteam
        self.tentruong = tentruong

    def __str__(self):
        return "{} {} {} {}".format(self.mathisinh, self.tenthisinh, self.tenteam, self.tentruong)


n = int(input())
team = dict()
for i in range(1, n+1):
    mateam = f"Team{i:02d}"
    tenteam = input()
    tentruong = input()
    team[mateam] = {'tenteam':tenteam, 'tentruong':tentruong}

dsTs = []
m = int(input())
for i in range(1, m+1):
    tenthisinh = input()
    mateam = input()
    dsTs.append(ThiSinh(i, tenthisinh, team[mateam]['tenteam'], team[mateam]['tentruong']))

dsTs.sort(key=lambda x : (x.tenthisinh))
print(*dsTs, sep='\n')
