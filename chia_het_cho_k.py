import math
a, k, n = [int(i) for i in input().split()]
x = math.ceil((1+a)/k)
y = math.floor(n/k)
if x-y>0:
    print(-1)
else:
    for i in range (x, y+1):
        print(k*i-a, end = " ")


