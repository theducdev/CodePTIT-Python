import math
t = int(input())
while t:
    n, x, m = [float(i) for i in input().split() ]
    t-=1
    print(math.ceil(math.log(m/n, 1+x/100)))
    