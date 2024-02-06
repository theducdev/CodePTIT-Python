ds = []
for _ in range(int(input())):
    ds.append(len(input().split()))
sobai = 0
theloai = []
i = 0
while i < len(ds):
    if ds[i] == 6:
        sobai+=1
        theloai.append(1)
        while i<len(ds) and (ds[i] == 6 or ds[i] == 8): i+=1
    elif ds[i] == 7:
        sobai+=1
        theloai.append(2)
        i+=4
print(sobai)
print(*theloai, sep='\n')
