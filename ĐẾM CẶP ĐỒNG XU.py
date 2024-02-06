import math
n = int(input())
a = [[i for i in input()] for _ in range(1, n+1)]
cnt = 0
for i in range(n):
    tmp1 = 0
    tmp2 = 0
    for j in range(n):
        if a[i][j] == 'C':
            tmp1+=1
        if a[j][i] =='C':
            tmp2+=1 
    if tmp1>=2:
        cnt+=math.comb(tmp1, 2)
    if tmp2>=2:
        cnt+=math.comb(tmp2, 2)

print(cnt)
